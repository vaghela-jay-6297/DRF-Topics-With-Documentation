from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from rest_framework import mixins
from APIview_ViewSet_app.models import Student
from rest_framework.response import Response
from APIview_ViewSet_app.serializer import NameSerializer, StudentSerializer

# APIView without model
class DemoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['RED', 'YELLOW', 'GREEN', 'ORANGE', 'BLUE', 'BLACK']
        return Response({'msg':'Color fetched.', 'colors':colors}) 
    
    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)  # get data from user side.
        if serializer.is_valid():   # check serializer validation if validation is complete then execute below code of if.
            name = serializer.data.get('name')  # get name field from serializer data
            msg = "Hello {}, Welocome.".format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status=400)  # send error message 
        
    def put(self, request, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from put method.'})
    
    def patch(self, request, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from patch method.'})

    def delete(self, request, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from delete method.'})
    
# ----------------------------------------------------------------------------------------------------------------------------------------    

# ViewSet without model
class DemoViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        colors = ['RED', 'YELLOW', 'GREEN', 'ORANGE', 'BLUE', 'BLACK']
        return Response({'msg':'Color fetched.', 'colors':colors}) 
    
    def create(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)  # get data from user side.
        if serializer.is_valid():   # check serializer validation if validation is complete then execute below code of if.
            name = serializer.data.get('name')  # get name field from serializer data
            msg = "Hello {}, Welocome.".format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status=400)  # send error message 

    # here pass primary key(pk) for destroy/update/partial_update/retrieve specified record.   
    def retrieve(self, request, pk=None, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from retrieve method.'})
        
    def update(self, request, pk=None, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from update method.'})
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from partial_update method.'})

    def destroy(self, request, pk=None, *args, **kwargs):
        # database not availble so just pass the response method for testing purpose.
        return Response({'msg':'This response from destroy method.'})

# ----------------------------------------------------------------------------------------------------------------------------------------    

# APIView with student model
'''
class StudentListAPIView(APIView):
    def get(self, request, format=None):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
'''

# using generic list apiview class 
class StudentListAPIView(generics.ListAPIView):
    # queryset = Student.objects.all()    # queryset built-in keyword
    serializer_class = StudentSerializer    # serializer_class built-in keyword

    # override get_queryset method for searching.
    def get_queryset(self):
        qs=Student.objects.all()   # get all records from DB
        name=self.request.GET.get('sname')  # get name from query string(in url like /?name:)
        if name is not None:   
            qs=qs.filter(sname__icontains=name) # filter records when sname row contain name. like sname=sunny
        return qs

# create a record into student table
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# get/fetch a record from student table
class StudentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# update/put/patch a record in student table
class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Delete a record in student table
class StudentDestroyAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

# list of records & create new record
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve Record & Update record
class StudentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field='id'   # update/retrieve records based on id field

# Retrieve Record & Destroy/Delete record
class StudentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field='id'   # destroy/retrieve records based on id field

# Retrieve Record & Destroy/Delete record & update record
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field='id'   # destroy/retrieve/update records based on id field


# ----------------------------------------------------------------------------------------------------------------------------------------

# at lease one APIView pass to the class when you use mixin.
class StudentListCreateModelMixin(mixins.CreateModelMixin, generics.ListAPIView):   # we can also use ListCreateAPIView.
    # here perform two operations get list & create new record using mixins
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # HTTP handler is post that's why we write post function and return create func.
    def post(self, request, *args, **kwargs):
        # create method comes from mixin class(parent class) we dont have to require other code.
        return self.create(request, *args, **kwargs)

# we can also use RetrieveUpdateDestroyAPIView.
class StudentRetrieveUpdateDestroyModelMixin(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # HTTP handler is put that's why we write put function and return update func.
    def put(self, request, *args, **kwargs):    
        # update method comes from mixin class(parent class) we dont have to require other code.
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)


