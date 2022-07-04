from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_details, name='staff-details')
]
