from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from NormalSerializer.models import Employee
from NormalSerializer.serializer import EmployeeSerializer

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class EmployeeCRUD(View):
    # using this single endpoint we get specified emp data and also get all employee data
    def get(self, request, *args, **kwargs): 
        json_data=request.body  # get data from user side
        stream = io.BytesIO(json_data)  # json data convert into bytes
        py_data = JSONParser().parse(stream)    # bytes convert into python native data like dict
        id = py_data.get('id', None )   # get id field from dict py_data if not found return None obj
        if id is not None:
            emp = Employee.objects.get(id=id)   # get data from DB
            serializer = EmployeeSerializer(emp)    # serializer emp data
            json_data = JSONRenderer().render(serializer.data)    # convert inton json data
            return HttpResponse(json_data, content_type="Application/json")
        all_emp = Employee.objects.all()    # get all employee data
        serializer = EmployeeSerializer(all_emp, many=True)    # serializer emp data
        json_data = JSONRenderer().render(serializer.data)    # convert inton json data
        return HttpResponse(json_data, content_type="Application/json")
    
    # post/create employee
    def post(self, request, *args, **kwargs):
        json_data=request.body  # get data from user side
        stream = io.BytesIO(json_data)  # json data convert into bytes
        py_data = JSONParser().parse(stream)    # bytes convert into python native data like dict
        serializer = EmployeeSerializer(data=py_data)
        if serializer.is_valid():   # check serializer's data are valid or not
            # employee created
            serializer.save()   # when we call save() method automaticall called create() method of serializer.py file.
            msg = {'msg': "User Created..."}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="Application/json")
        # if serializer is invalid then give serializer errors to user
        json_data = JSONRenderer().render(serializer.errors)   
        return HttpResponse(json_data, content_type="Application/json") 
    
    # update employee
    def put(self, request, *args, **kwargs):
        json_data=request.body  # get data from user side
        stream = io.BytesIO(json_data)  # json data convert into bytes
        py_data = JSONParser().parse(stream)    # bytes convert into python native data like dict
        id = py_data.get('id')  # fetch id field from user's data
        emp = Employee.objects.get(id=id)   # get that id data from DB
        # full update & partial update both are working. we set partial is True.
        serializer = EmployeeSerializer(emp, py_data, partial=True) # emp is old data; py_data is new data
        if serializer.is_valid():   # check serializer's data are valid or not
            # employee updated
            serializer.save()   # when we call save() method automaticall called update() method of serializer.py file.
            msg = {'msg': "User Record Updated..."}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type="Application/json")
        # if serializer is invalid then give serializer errors to user
        json_data = JSONRenderer().render(serializer.errors)   
        return HttpResponse(json_data, content_type="Application/json") 
    
    # delete employee
    def delete(self, request, *args, **kwargs):
        json_data=request.body  # get data from user side
        stream = io.BytesIO(json_data)  # json data convert into bytes
        py_data = JSONParser().parse(stream)    # bytes convert into python native data like dict
        id = py_data.get('id')  # fetch id field from user's data
        emp = Employee.objects.get(id=id)   # get that id data from DB
        emp.delete()    # delete emp object
        msg = {'msg': "User Record Deleted..."}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type="Application/json")
