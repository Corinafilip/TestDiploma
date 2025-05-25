from rest_framework import generics, permissions, status
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta

from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer
from django.db.models import Prefetch
from .utils import can_cancel

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


class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, booking_id):
        ...


class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, renter=request.user)
        except Booking.DoesNotExist:
            return Response({"detail": "Booking not found."}, status=404)

        if booking.is_cancelled:
            return Response({"detail": "Booking is already cancelled."}, status=400)

        # Check if cancellation is allowed (e.g., at least 1 day before check-in)
        if timezone.now() >= booking.check_in - timedelta(days=1):
            return Response({"detail": "Cancellation deadline has passed."}, status=400)

        booking.is_cancelled = True
        booking.cancelled_at = timezone.now()
        booking.save()

        return Response({"detail": "Booking successfully cancelled."}, status=200)

#if not can_cancel(booking):
#    ...