# patient/models.py
from django.db import models
from django.core.validators import RegexValidator

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^(97|98)\d{8}$',
                message="Enter a valid Nepali phone number (10 digits starting with 97 or 98)."
            )
        ],
        unique=True
    )
    password = models.CharField(max_length=255)  # Use hashed passwords later
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')  # Store ad images
    link = models.URLField()  # Redirect to hospital or other relevant links

    def __str__(self):
        return self.title

