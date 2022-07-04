from django.forms import ModelForm
from django import forms
from .models import *


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


