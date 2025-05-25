from django.urls import path
from .views import BookingListCreateView, BookingReceivedListView, CancelBookingView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
    path('received/', BookingReceivedListView.as_view(), name='booking-received-list'),
    path('cancel/', CancelBookingView.as_view(), name='booking-cancel'),path('cancel/<int:booking_id>/', CancelBookingView.as_view(), name='cancel-booking'),

]
