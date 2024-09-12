from django.urls import path, include
from Viewsets_app import views
from rest_framework.authtoken.views import obtain_auth_token     # normal token authentication(built-in)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView   # JWT token(3rd party module)
from authentication_n_authorization_app.views import EmployeeCRUD, StudentCRUD, StudentCRUDJWT, StudentCustomAUthentication
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emp-data', EmployeeCRUD) # basename is optional when you use modelViewset class.
router.register('stu-data', StudentCRUD)    # custom permission
router.register('stu-jwt', StudentCRUDJWT, basename="JWT test") # get data using JWT token based process
router.register('stu-custom-auth', StudentCustomAUthentication, basename="custom-uthentication")    # custom authentication

urlpatterns = [
    path('', include(router.urls)),  # to access employee data not working without token nd permission

    # here obtain_auth_token FBV is a part of authtoken for generate user a token. 
    path('get-api-token/', obtain_auth_token, name='get-api-token'), # normal token based authentication

    # JWT token authentication.
    path('auth-jwt/', TokenObtainPairView.as_view(), name='token_obtain'), # get jwt token with passing username & password. 
    path('auth-jwt-refresh/', TokenRefreshView.as_view(), name='token_refresh'), # get refresh token or get new updated access token   
    path('auth-jwt-verify/', TokenVerifyView.as_view(), name='token_verify'), # to verify token
]