from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Viewsets_app import views

router = DefaultRouter()
# router.register('modelViewset', views.EmployeeCRUD_CBV, base_name='modelViewset') # base_name define when you use Viewset Class
router.register('modelViewset', views.EmployeeCRUD_CBV) # base_name is optional when you use modelViewset class.

urlpatterns = [
    path('', include(router.urls)),
]