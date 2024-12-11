from django import forms
from .models import Hospital, Doctor, DoctorSchedule, Ambulance
from django.core.exceptions import ValidationError

def validate_pan_number(value):
    if not value.isdigit() or len(value) != 9:
        raise ValidationError('PAN number must be exactly 9 digits.')

class HospitalSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number', 'email', 'pan_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_pan_number(self):
        pan_number = self.cleaned_data.get('pan_number')
        validate_pan_number(pan_number)
        return pan_number


class HospitalLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number', 'email', 'website', 'description']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialty', 'phone_number', 'email', 'available']


class DoctorScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = ['start_time', 'end_time', 'days_available']


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['ambulance_number', 'driver_name', 'contact_number', 'available']
