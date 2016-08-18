from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from models import WaitlistEntry

from waitlist_entries.forms import WaitlistEntryForm


def index(request):
    if request.method == 'POST':
        waitlist_entry_form = WaitlistEntryForm(request.POST)

        if waitlist_entry_form.is_valid():
            email = waitlist_entry_form.cleaned_data['email']
            waitlist_entry = WaitlistEntry.objects.create(email=email)
            redirect(reverse('waitlist_entries:index'))

    else:
        waitlist_entry_form = WaitlistEntryForm()

    waitlist_entries = WaitlistEntry.objects.all()
    context = {
        'waitlist_entries': waitlist_entries,
        'waitlist_entry_form': waitlist_entry_form
    }
    return render(request, 'waitlist_entries/index.html', context)
