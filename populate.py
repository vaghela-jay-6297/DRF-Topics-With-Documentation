# generate fake data for vendor table.
import os
# here we pass DJANGO_SETTINGS_MODULE & project_name.settings 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTopicProject.settings')
import django
django.setup()

from pagination_app.models import Vendor
from faker import Faker
from random import *

faker = Faker()
def populate(n):
    # generate some fake data value of n.
    for i in range(n):
        fvno = randint(1001, 9999)  # random value generate from 1001 to 9999.
        fvname = faker.name()   # generate fake name
        fvsal = randint(10000, 45000)   # random value generate from 10000 to 45000.
        fvaddr = faker.city()   # generate fake city
        print(fvno, fvname, fvsal, fvaddr)
        vendor_record = Vendor.objects.get_or_create(vno=fvno,
                                                     vname=fvname,
                                                     vsal=fvsal,
                                                     vaddr=fvaddr)
    
populate(120) # fun calling with passing value. value is basiclly records value. how many records you want.


