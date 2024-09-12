from django.urls import path
from NormalSerializer import views

urlpatterns = [
    path('api/',  views.EmployeeCRUD.as_view()),
]