"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import employee_view, employee_details_view, manager_form_view, employee_update, employee_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee_view, name='employee-list'),
    path('employeeupdate/<int:pk>/', employee_update, name='employee-update'),
    path('employeedelete/<int:pk>/', employee_delete, name='employee-delete'),
    path('employeedetails/<int:pk>/', employee_details_view, name='employee-details'),
    path('managerform',manager_form_view),

]
