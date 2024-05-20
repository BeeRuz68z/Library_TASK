from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from .views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(),name='token_verify'),
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register_view,name='register'),
]