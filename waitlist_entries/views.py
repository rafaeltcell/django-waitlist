import json

import addressbook_pb2

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from django.views.decorators.csrf import csrf_exempt

from waitlist_entries.models import WaitlistEntry

from waitlist_entries.forms import WaitlistEntryForm



def index(request):
    address_book = addressbook_pb2.AddressBook()
    try:
        with open("ma-book", "rb") as ma_book_file:
            address_book.ParseFromString(ma_book_file.read())
    except IOError:
        print ": File not found.  Creating a new file."
    # print address_book.SerializeToString()

    import logging
    import httplib as http_client

    http_client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    import requests
    r = requests.post('http://192.168.99.100:3000/waitlist_entries/create_ab/', address_book.SerializeToString())

    if request.method == 'POST':
        waitlist_entry_form = WaitlistEntryForm(request.POST)

        if waitlist_entry_form.is_valid():
            email = waitlist_entry_form.cleaned_data['email']
            WaitlistEntry.objects.create(email=email)
            redirect(reverse('waitlist_entries:index'))

    else:
        waitlist_entry_form = WaitlistEntryForm()

    waitlist_entries = WaitlistEntry.objects.all()
    context = {
        'waitlist_entries': waitlist_entries,
        'waitlist_entry_form': waitlist_entry_form
    }
    return render(request, 'waitlist_entries/index.html', context)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = request.POST

        print("LSKDJFLKDJSF")
        print(request.body)
        print(data)
        print("LSKDJFLKDJSF")

        if not data:
            try:
                data = json.loads(request.body)
            except Exception as e:
                pass

        waitlist_entry_form = WaitlistEntryForm(data)

        if waitlist_entry_form.is_valid():
            email = waitlist_entry_form.cleaned_data['email']
            waitlist_entry = WaitlistEntry.objects.create(email=email)
            return HttpResponse(
                    json.dumps({"id": waitlist_entry.id, "email": waitlist_entry.email}),
                    content_type='application/json')
        else:
            return HttpResponse(waitlist_entry_form.errors.as_json(), content_type='application/json')

    else:
        return HttpResponseBadRequest()

@csrf_exempt
def create_ab(request):
    if request.method == 'POST':
        address_book = addressbook_pb2.AddressBook()
        address_book.ParseFromString(request.body)

        print "LSKDJFLKDJSF"
        print address_book.SerializeToString()
        print "LSKDJFLKDJSF"

        return HttpResponse(
            json.dumps({"success": True,}),
            content_type='application/json')

        # if not data:
            # try:
                # data = json.loads(request.body)
            # except Exception as e:
                # pass

        # waitlist_entry_form = WaitlistEntryForm(data)

        # if waitlist_entry_form.is_valid():
            # email = waitlist_entry_form.cleaned_data['email']
            # waitlist_entry = WaitlistEntry.objects.create(email=email)
            # return HttpResponse(
                    # json.dumps({"id": waitlist_entry.id, "email": waitlist_entry.email}),
                    # content_type='application/json')
        # else:
            # return HttpResponse(waitlist_entry_form.errors.as_json(), content_type='application/json')

    else:
        return HttpResponseBadRequest()
