import json

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from django.views.decorators.csrf import csrf_exempt

from waitlist_entries.models import WaitlistEntry

from waitlist_entries.forms import WaitlistEntryForm


def index(request):
    if request.method == 'POST':
        waitlist_entry_form = WaitlistEntryForm(request.POST)

        if waitlist_entry_form.is_valid():
            email = waitlist_entry_form.cleaned_data['email']
            WaitlistEntry.objects.create(email=email)
            redirect(reverse('waitlist_entries:index'))

    else:
        from tcell_hooks.v1 import send_django_login_event, LOGIN_SUCCESS, LOGIN_FAILURE

        send_django_login_event(
            status=LOGIN_SUCCESS,
            django_request=request,
            user_id="waitlist_entries+index_success@tcell.io",
            session_id="124KDJFL3234")
        send_django_login_event(
            status=LOGIN_FAILURE,
            django_request=request,
            user_id="waitlist_entries+index_failure@tcell.io",
            session_id="124KDJFL3234")

        from tcell_hooks.v1 import send_login_event

        send_login_event(
            status=LOGIN_SUCCESS,
            session_id="124KDJFL3234",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) ...",
            referrer="http://192.168.99.100:3000/",
            remote_address="192.168.99.1",
            header_keys=["HOST", "USER_AGENT", "ACCEPT", "REFERER", "ACCEPT_ENCODING", "ACCEPT_LANGUAGE", "COOKIE"],
            user_id="waitlist_entries+non_django_success@tcell.io",
            document_uri="/users/auth/doorkeeper/callbackuri")
        send_login_event(
            status=LOGIN_FAILURE,
            session_id="124KDJFL3234",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) ...",
            referrer="http://192.168.99.100:3000/",
            remote_address="192.168.99.1",
            header_keys=["HOST", "USER_AGENT", "ACCEPT", "REFERER", "ACCEPT_ENCODING", "ACCEPT_LANGUAGE", "COOKIE"],
            user_id="waitlist_entries+non_django_failure@tcell.io",
            document_uri="/users/auth/doorkeeper/callbackuri")

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

        if not data:
            try:
                data = json.loads(request.body)
            except Exception as e:
                print "Error parsing request body: {e}".format(e=e)

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
