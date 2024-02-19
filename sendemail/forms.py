from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))