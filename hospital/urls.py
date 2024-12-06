from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_hospital/', views.manage_hospital, name='manage_hospital'),
    path('edit_hospital/<int:pk>/', views.edit_hospital, name='edit_hospital'),
    path('manage_doctors/', views.manage_doctors, name='manage_doctors'),
    path('edit_doctor_schedule/<int:pk>/', views.edit_doctor_schedule, name='edit_doctor_schedule'),
    path('manage_ambulances/', views.manage_ambulances, name='manage_ambulances'),
]
