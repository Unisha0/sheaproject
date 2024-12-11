# patient/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Patient, Advertisement
from .forms import PatientSignupForm, PatientLoginForm

def signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.password = make_password(form.cleaned_data['password'])
            patient.save()
            return redirect('patient_login')
    else:
        form = PatientSignupForm()
    return render(request, 'patient/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            try:
                patient = Patient.objects.get(phone_number=phone_number)
                if check_password(password, patient.password):
                    request.session['patient_id'] = patient.id
                    return redirect('patient_dashboard')
                else:
                    form.add_error(None, 'Invalid credentials')
            except Patient.DoesNotExist:
                form.add_error(None, 'Patient not found')
    else:
        form = PatientLoginForm()
    return render(request, 'patient/login.html', {'form': form})


def dashboard(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient_login')

    patient = Patient.objects.get(id=patient_id)
    ads = Advertisement.objects.all()
    return render(request, 'patient/dashboard.html', {'patient': patient, 'ads': ads})
