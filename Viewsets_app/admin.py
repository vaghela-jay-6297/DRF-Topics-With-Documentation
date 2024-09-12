from django.contrib import admin
from Viewsets_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)