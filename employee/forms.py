from django.forms import ModelForm
from .models import Managers, Employee

class ManagerForm(ModelForm):
	class Meta:
		model = Managers
		fields = '__all__'

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'