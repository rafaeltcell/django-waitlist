from django import forms

class WaitlistEntryForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=255)
