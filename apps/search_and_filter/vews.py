from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from apps.rent.models import Rent
from apps.rent.serializer import RentSerializer
from .filters import RentFilter


class RentSearchFilterView(generics.ListAPIView):
    serializer_class = RentSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Rent.objects.filter(is_active=True, is_deleted=False) \
                           .select_related('owner')

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterSet_class = RentFilter
    ordering_fields = ['price_per_night', 'created_at']
