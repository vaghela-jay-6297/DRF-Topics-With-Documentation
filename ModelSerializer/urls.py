from django.urls import path
from ModelSerializer import views

urlpatterns = [
    path('modelserializer/',  views.EmployeeCRUD.as_view()),
]