from django.http import HttpResponseForbidden
from django.shortcuts import render

from waitlist_entries.models import WaitlistEntry

def search(request):
    if request.method == 'POST':
        return HttpResponseForbidden()

    if None is request.GET.get('q'):
        waitlist_entries = []
    else:
        query = "select * from waitlist_entries_waitlistentry where email = '%s'"  % request.GET.get('q')
        waitlist_entries = WaitlistEntry.objects.raw(query)

    print(waitlist_entries)
    context = {
        'waitlist_entries': waitlist_entries
    }
    return render(request, 'vulnerabilities/search.html', context)

def sql_exception(request):
    for p in WaitlistEntry.objects.raw("select * from wailskfdj"):
        print(p)
