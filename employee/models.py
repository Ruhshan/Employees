from django.db import models

# Create your models here.


GENDER_LIST = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other'),
	)

class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30, blank=True, null=True)
	last_name = models.CharField(max_length=30)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	dob = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_LIST)
	contact = models.CharField(max_length=15)
	address = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.first_name