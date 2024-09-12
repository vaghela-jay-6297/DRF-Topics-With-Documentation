from django.urls import path, include
from pagination_app import views

urlpatterns = [
    path('',  views.VendorListView.as_view()),  # url for pagination VendorListView class
]