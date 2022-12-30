from django.shortcuts import render
from playground.models import *


# Create your views here.

def index_view(request):
    return render(request, 'playground/index.html')
def employees_list(request):
    employee = Employee.objects.all()
    return render(request, 'playground/employees.html', {'obj': employee})

