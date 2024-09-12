"""
URL configuration for djangoTopicProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NormalSerializer.urls')), # url for NormalSerializer App
    path('api/', include('ModelSerializer.urls')),  # url for ModelSerializer App
    path('api2/', include('APIview_ViewSet_app.urls')),  # url for APIview_ViewSet_app App (genericView, mixins)
    # path('api3/', include('Viewsets_app.urls')),    # url for Viewsets_app App
    path('api4/', include('authentication_n_authorization_app.urls')),    # url for authentication_n_authorization_app App
    path('api5/', include('pagination_app.urls')),   # url for pagination_app application
    path('api6/', include('DRF_filtering_app.urls')),   # url for DRF_filtering_app application
    path('api7/', include('NestedSerializer_app.urls')),   # url for NestedSerializer_app application
    # swagger API tool
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
