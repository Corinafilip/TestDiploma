from django_filters import rest_framework as filters
from apps.rent.models import Rent
from django.db.models import Q


class RentFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price_per_night", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price_per_night", lookup_expr='lte')
    rooms_min = filters.NumberFilter(field_name="rooms_count", lookup_expr='gte')
    rooms_max = filters.NumberFilter(field_name="rooms_count", lookup_expr='lte')
    room_type = filters.CharFilter(field_name="room_type", lookup_expr='iexact')
    location = filters.CharFilter(field_name="address", lookup_expr='icontains')
    keyword = filters.CharFilter(method='filter_keyword')

    ordering = filters.OrderingFilter(
        fields=(
            ('price_per_night', 'price'),
            ('created_at', 'created'),
        ),
        field_labels={
            'price': 'Цена',
            'created': 'Дата добавления',
        }
    )

    class Meta:
        model = Rent
        fields = []

    def filter_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value)
        )



