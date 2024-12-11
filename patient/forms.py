# patient/forms.py
from django import forms
from .models import Patient

class PatientSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone_number', 'password']


class PatientLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
