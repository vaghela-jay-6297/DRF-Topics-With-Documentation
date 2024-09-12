from django.contrib import admin
from pagination_app.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display=['id','vno', 'vname','vsal','vaddr']

admin.site.register(Vendor, VendorAdmin)
