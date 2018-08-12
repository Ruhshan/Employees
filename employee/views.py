from django.shortcuts import render, redirect
from .models import Employee, Managers
from .forms import ManagerForm, EmployeeForm
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

def manager_form_view(request):
	if request.method == 'GET':
			form = ManagerForm()
			return render(request, 'manager_form.html', {'form':form})
	else:
		first_name = request.POST['first_name']
		middle_name = request.POST['middle_name']
		last_name = request.POST['last_name']
		
		Managers.objects.create(first_name = first_name, middle_name =middle_name,
			last_name = last_name)
		form = ManagerForm()
		return render(request, 'manager_form.html', {'form':form})

def employee_update(request, pk):
	if request.method == 'GET':
		employee =  Employee.objects.get(id=pk)
		form = EmployeeForm(instance = employee)
		return render(request, 'employeeform.html', {'form':form})
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('employee-list')
		return render(request, 'employeeform.html', {'form':form})

def employee_delete(request, pk):
	employee = Employee.objects.get(id=pk)
	employee.delete()
	return redirect('employee-list')


