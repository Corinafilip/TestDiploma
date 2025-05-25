from django.urls import path
from .views import RentListCreateAPIView, RentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('rents/', RentListCreateAPIView.as_view(), name='rent-list-create'),
    path('rents/<int:pk>/', RentRetrieveUpdateDestroyAPIView.as_view(), name='rent-detail'),
]
