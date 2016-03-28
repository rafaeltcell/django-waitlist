from django.shortcuts import render

from models import WaitlistEntry


def index(request):
    waitlist_entries = WaitlistEntry.objects.all()
    context = {
        'waitlist_entries': waitlist_entries,
    }
    return render(request, 'waitlist_entries/index.html', context)
