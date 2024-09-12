from django.contrib import admin
from APIview_ViewSet_app. models import Student

# Register your models here.
class StudentApdmin(admin.ModelAdmin):
    list_display=['id', 'sno','sname', 'smark', 'saddr']

admin.site.register(Student, StudentApdmin)
