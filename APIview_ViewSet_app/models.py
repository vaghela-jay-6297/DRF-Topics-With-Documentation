from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=64)
    smark=models.FloatField()
    saddr=models.CharField(max_length=64)

    def __str__(self):
        return str(self.sno) + str(self.sname)