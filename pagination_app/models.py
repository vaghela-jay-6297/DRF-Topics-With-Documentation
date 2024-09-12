from django.db import models

# Create your models here.
class Vendor(models.Model):
    vno=models.IntegerField()
    vname=models.CharField(max_length=64)
    vsal=models.FloatField()
    vaddr=models.CharField(max_length=64)

    def __str__(self):
        return str(self.vno) + str(self.vname)