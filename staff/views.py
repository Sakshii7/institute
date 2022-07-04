from django.shortcuts import render
from staff.forms import StaffForm
from django.shortcuts import HttpResponse, render


# Create your views here.


def staff_details(request):
    if request.method == 'POST':
        details = StaffForm(request.POST)

        if details.is_valid():
            staff_data = details.save(commit=False)
            staff_data.save()
            return HttpResponse("Data Submitted Successfully.")
        else:
            return render(request, "staff.html", {"form": details})
    else:
        form = StaffForm(None)
        return render(request, "staff.html", {"form": form})



