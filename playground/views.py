from django.shortcuts import render
from playground.models import * 

# Create your views here.

def employees_list(request):
    employee = Employee.objects.all()
    return render(request, 'playground/index.html', {'obj': employee})