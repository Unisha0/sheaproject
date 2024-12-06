from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital, Doctor, DoctorSchedule, Ambulance
from .forms import HospitalForm, DoctorForm, DoctorScheduleForm, AmbulanceForm


def dashboard(request):
    # For now, just use the first hospital; you can adjust the logic as needed
    hospital = Hospital.objects.first()
    return render(request, 'hospital/dashboard.html', {'hospital': hospital})

def manage_hospital(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital/manage_hospital.html', {'hospitals': hospitals})


def edit_hospital(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('manage_hospital')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital/edit_hospital.html', {'form': form})


def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/manage_doctors.html', {'doctors': doctors})


def edit_doctor_schedule(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if hasattr(doctor, 'schedule'):
        schedule = doctor.schedule
    else:
        schedule = None

    if request.method == "POST":
        form = DoctorScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.doctor = doctor
            schedule.save()
            return redirect('manage_doctors')
    else:
        form = DoctorScheduleForm(instance=schedule)
    return render(request, 'hospital/edit_doctor_schedule.html', {'form': form})


def manage_ambulances(request):
    ambulances = Ambulance.objects.all()
    return render(request, 'hospital/manage_ambulances.html', {'ambulances': ambulances})
