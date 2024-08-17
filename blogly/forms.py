from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label='Name', max_length=100, required=True)
    email=forms.CharField(label='Email', required=True)
    message=forms.CharField(label='Message', required=True)
    