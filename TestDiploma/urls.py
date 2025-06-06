"""
URL configuration for TestDiploma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.user.views import (
    RegisterUserAPIView, CurrentUserAPIView, LogoutView,
    UpdateUserAPIView, ChangePasswordAPIView, AdminUserListAPIView
)


urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls')),
    path('api/bookings/', include('apps.bookings.urls')),
    path('api/search/', include('apps.search_and_filter.urls')),
    path('api/rent/', include('apps.rent.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    # path('admin/', admin.site.urls),  # 👈 this is required
    # path('', include('apps.rent.urls')),  # or your app's urls

]
