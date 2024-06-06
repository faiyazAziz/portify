from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)