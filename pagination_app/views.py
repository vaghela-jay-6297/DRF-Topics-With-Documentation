from django.shortcuts import render
from pagination_app.models import Vendor
from pagination_app.serializer import VensorSerializer
from rest_framework import generics
from pagination_app.pagination import MyPagination, MyPagination2, MyPagination3  # import from pagination file 

class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VensorSerializer
    
    # localling define or override global variable
    # pagination_class = PageNumberPagination

    # implement custom pagination class.
    # pagination_class = MyPagination # pagenumberpagination example
    # pagination_class = MyPagination2    # limitoffsetpagination
    pagination_class = MyPagination3    # CursonPagination
    