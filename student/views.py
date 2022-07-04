from django.shortcuts import render
from django.shortcuts import HttpResponse, render


# Create your views here.
from student.forms import StudentForm


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


