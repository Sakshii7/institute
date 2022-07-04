from django.forms import ModelForm
from django import forms
from student.models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean(self):
        super(StudentForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        text = self.cleaned_data.get('text')

        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class([
                'Minimum 3 character required'
            ])

        return self.cleaned_data
