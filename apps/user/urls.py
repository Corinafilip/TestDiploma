from django.urls import path
from .views import RegisterUserAPIView, CurrentUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='user-register'),
    path('me/', CurrentUserAPIView.as_view(), name='user-detail'),
]
