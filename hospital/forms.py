from django import forms
from .models import Hospital, Doctor, DoctorSchedule, Ambulance


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
