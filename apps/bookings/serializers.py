from rest_framework import serializers
from apps.bookings.models import Booking
from apps.rent.models import Rent
from apps.user.models import User


class BookingSerializer(serializers.ModelSerializer):
    rent_title = serializers.CharField(source='rent.title', read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    renter_username = serializers.CharField(source='renter.username', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'rent', 'rent_title',
            'check_in', 'check_out',
            'property_address', 'room_type', 'guests',
            'total_price', 'paid', 'is_cancelled', 'cancelled_at',
            'is_confirmed', 'owner', 'owner_username',
            'renter', 'renter_username',
            'created_at',
        ]
        read_only_fields = ['owner', 'renter', 'property_address', 'room_type']


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['rent', 'check_in', 'check_out', 'guests', 'total_price']

    def create(self, validated_data):
        user = self.context['request'].user
        rent = validated_data['rent']

        booking = Booking.objects.create(
            rent=rent,
            check_in=validated_data['check_in'],
            check_out=validated_data['check_out'],
            guests=validated_data.get('guests'),
            total_price=validated_data['total_price'],
            paid=False,
            is_cancelled=False,
            is_confirmed=False,
            property_address=rent.address,
            room_type=rent.room_type,
            renter=user,
            owner=rent.owner,
        )
        return booking
