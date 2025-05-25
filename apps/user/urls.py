from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterUserAPIView,
    CurrentUserAPIView,
    LogoutView,
    UpdateUserAPIView,
    ChangePasswordAPIView,
)

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='user-register'),
    path('me/', CurrentUserAPIView.as_view(), name='user-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/update/', UpdateUserAPIView.as_view(), name='user-update'),
    path('me/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),


]
