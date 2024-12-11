# patient/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='patient_signup'),
    path('login/', views.login, name='patient_login'),
    path('dashboard/', views.dashboard, name='patient_dashboard'),
]
