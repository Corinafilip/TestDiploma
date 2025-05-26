from django.utils import timezone
from rest_framework import generics, permissions
from models import Review
from serializers import ReviewSerializer
from apps.rent.permissions import HasCompletedBooking


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, HasCompletedBooking]

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        # Add timestamp to request object
        request.timestamp = timezone.now()
        return super().dispatch(request, *args, **kwargs)