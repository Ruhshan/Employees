from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_view(request):

	employee_list = Employee.objects.all()
	context = {
		'employee_list': employee_list
	}
	return render(request,'employee.html', context)


def employee_details_view(request, pk):

	employee = Employee.objects.get(id=pk)
	context = {
		'employee': employee
	}
	return render(request,'details.html', context)
