from django.contrib import admin
from .models import *

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'date')
    search_fields = ['first_name']
    inlines = [ChoiceInLine]


admin.site.register(Student, StudentAdmin)

