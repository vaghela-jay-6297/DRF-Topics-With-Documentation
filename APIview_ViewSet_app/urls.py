from django.urls import path, include
from APIview_ViewSet_app import views
from rest_framework.routers import DefaultRouter

# router only required for viewsets 
router = DefaultRouter()
router.register('test-viewset', views.DemoViewSet, basename='test-viewset') # register router without model

urlpatterns = [
    # Viewsets
    # include viewsets router into url
    path('', include(router.urls)), # make url for router viewset

    # APIView
    # With out model simple APIView & Viewset
    path('apiview/',  views.DemoAPIView.as_view()), # ulr for apiview
    
    # GenericAPIView
    # with model using GenericAPIView
    path('apiview2/', views.StudentListAPIView.as_view()),  # list of student, get searched records
    path('apiview2/create/', views.StudentCreateAPIView.as_view()),  # create/post record into DB
    path('apiview2/retrieve/<int:pk>', views.StudentRetrieveAPIView.as_view()),  # get/fetch record from DB
    path('apiview2/update/<int:pk>', views.StudentUpdateAPIView.as_view()),  # update record in DB
    path('apiview2/delete/<int:id>', views.StudentDestroyAPIView.as_view()),  # delete record in DB
    # combine two genericviews in a single url.
    path(r'apiview2/list_create/$', views.StudentListCreateAPIView.as_view()),  # get list & create new record, $ denote the end of a URL pattern
    path('apiview2/retrieve_update/<int:id>', views.StudentRetrieveUpdateAPIView.as_view()),  # get record & update records
    path('apiview2/retrieve_destroy/<int:id>', views.StudentRetrieveDestroyAPIView.as_view()),  # get record & destroy records
    # combine three genericviews in a single url.
    path('apiview2/retrieve_update_destroy/<int:id>', views.StudentRetrieveUpdateDestroyAPIView.as_view()),  # get record & update records & destroy record.

    # Mixins
    path('apiview2/list_create_mixin', views.StudentListCreateModelMixin.as_view()), # to get records & create new record
    path('apiview2/retrieve_update_destroy_mixin/<int:pk>', views.StudentRetrieveUpdateDestroyModelMixin.as_view()), # to retrieve record detail & update & destroy record

]