from django.shortcuts import render
from django.shortcuts import HttpResponse, render


# Create your views here.
from student.forms import *


def index(request):
    if request.method == 'POST':
        details = StudentForm(request.POST)

        if details.is_valid():

            student_data = details.save(commit=False)
            student_data.save()

            return HttpResponse("Data Submitted Successfully")

        else:
            return render(request, "homepage.html", {"form": details})

    else:

        form = StudentForm(None)
        return render(request, "homepage.html", {"form": form})


def testing(request):
    if request.method == 'POST':
        details = TestingForm(request.POST)

        if details.is_valid():

            return HttpResponse("Data Submitted Successfully")

        else:
            return render(request, "testing.html", {"form": details})

    else:

        form = TestingForm(None)
        return render(request, "testing.html", {"form": form})

