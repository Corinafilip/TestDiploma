from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer
from django.db.models import Prefetch


class BookingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        return BookingSerializer

    def get_queryset(self):
        return Booking.objects.select_related('rent', 'owner', 'renter').filter(renter=self.request.user)

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)

class BookingReceivedListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.select_related('rent', 'owner', 'renter').filter(owner=self.request.user)
