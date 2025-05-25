from django.urls import path
from .views import BookingListCreateView, BookingReceivedListView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
    path('received/', BookingReceivedListView.as_view(), name='booking-received-list'),
]
