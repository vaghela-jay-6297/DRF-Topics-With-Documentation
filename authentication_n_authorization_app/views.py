from django.shortcuts import render
from authentication_n_authorization_app.serializer import EmployeeSerializer
from APIview_ViewSet_app.serializer import StudentSerializer
from Viewsets_app.models import Employee
from APIview_ViewSet_app.models import Student
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# import custom authentication
from authentication_n_authorization_app.authentications import CustomAuthentication, CustomAuthentication2 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication_n_authorization_app. permissions import IsReadOnly, IsGetOrPatch  # import custom/own permission

# token based authentication required and user must be authenticated without token and permission not get/access employee data or below class.
class EmployeeCRUD(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # authentication_classes, permission_classes keywords is built-in keywords
    authentication_classes = [TokenAuthentication,] # tuple & list both are working

    permission_classes = [IsAuthenticated,] # tuple & list both are working
    # permission_classes = [IsAdminUser,] # only admin user access this class.

# in below class we apply custom/own permission which is get from permissions.py file.
class StudentCRUD(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes, permission_classes keywords is built-in keywords
    authentication_classes = [TokenAuthentication,] # tuple & list both are working

    # permission_classes = [IsReadOnly, ]   # our own permission class for read only data
    permission_classes = [ IsGetOrPatch, ]   # our own permission class for read only & patch only methods allow.

# this class only create for testing JWT token based authentication
class StudentCRUDJWT(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # JWT token based authentication
    authentication_classes = [JWTAuthentication, ]

    permission_classes = [IsAuthenticated, ]

# in class we implement custom/own authentication
class StudentCustomAUthentication(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [CustomAuthentication, ]   # implement custom authentication
    authentication_classes = [CustomAuthentication2, ]   # implement second custom authentication
    permission_classes = (IsAuthenticated, )