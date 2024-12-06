from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='doctors', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    available = models.BooleanField(default=True) #project 

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"


class DoctorSchedule(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='schedule')
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_available = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.doctor.first_name}'s Schedule"


class Ambulance(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='ambulances', on_delete=models.CASCADE)
    ambulance_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Ambulance {self.ambulance_number} - {self.driver_name}"
