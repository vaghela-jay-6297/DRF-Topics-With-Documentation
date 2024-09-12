from django.shortcuts import render
from pagination_app.serializer import VensorSerializer
from pagination_app.models import Vendor
from rest_framework import generics

# Create your views here.
class VendorListAPI(generics.ListAPIView):
    queryset = Vendor.objects.all()   # we dont have to write this line because we override get_queryset() method.
    serializer_class = VensorSerializer
    ordering_fields = ('vsal', 'vaddr') # ordering records based on this fields. default value is '__all__'
    search_fields = ('vname',)  # contains 
    # search_fields = ('vname','vno)   # vname | vno (perform or operation here.) 
    # search_fields = ('^vname',) # starts with
    # search_fields = ('=vname',) # exact match

    ''' Planin Vanilla Filtering '''
    # def get_queryset(self): # override method.
    #     qs = Vendor.objects.all()
    #     name = self.request.GET.get('vname')
    #     if name is not None:
    #         qs = qs.filter(vname__icontains=name)
    #     return qs