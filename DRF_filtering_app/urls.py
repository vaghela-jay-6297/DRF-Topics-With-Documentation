from django.urls import path, include
from DRF_filtering_app import views

urlpatterns = [
    path('',  views.VendorListAPI.as_view()),  # url for pagination VendorListView class
]