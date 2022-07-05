from django.forms import ModelForm
from django import forms
from django.urls import reverse

from student.models import *
from crispy_forms.bootstrap import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "email", "roll_number"]

    def clean(self):
        super(StudentForm, self).clean()

        first_name = self.cleaned_data.get('first_name')

        if len(first_name) < 2:
            self._errors['first_name'] = self.error_class([
                'Minimum 3 character required'
            ])

        return self.cleaned_data


class TestingForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=200)
    address = forms.CharField(max_length=1000, widget=forms.Textarea())
    more_info = forms.CharField(max_length=1000, required=False,widget=forms.Textarea())
    color = forms.TypedChoiceField(
        label="Choose color",
        choices=((0, "Red"), (1, "Blue"), (2, "Green")),
        widget=forms.RadioSelect,
        initial='0',
        required=True)

    def __init__(self, *args, **kwargs):
        super(TestingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-personal-data-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('testing')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-18'
        self.helper.field_class = 'col-lg-18'
        self.helper.layout = Layout(
            Fieldset('Name',
                     Field('first_name', placeholder='Your first name', css_class="some-class"),
                     Div('last_name', title="Your last name"), ),
            Fieldset('Contact data', 'email', 'phone', style="color:brown;"),
            InlineRadios('color'),
            TabHolder(Tab('Address', 'address'),
                      Tab('More Info', Field('more_info', css_class="extra"))),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-success')),

            )
