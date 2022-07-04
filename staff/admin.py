from django.contrib import admin
from .models import *

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'gender')


admin.site.register(Staff, StaffAdmin)
