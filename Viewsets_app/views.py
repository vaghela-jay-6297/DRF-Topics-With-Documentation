from django.shortcuts import render
from rest_framework import viewsets
from Viewsets_app.models import Employee
from Viewsets_app.serializer import EmployeeSerializer 

# Create your views here.
class EmployeeCRUD_CBV(viewsets.ModelViewSet):
    # we can able to perform all opertions ok create, list, get, update,delete using below two lines.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer