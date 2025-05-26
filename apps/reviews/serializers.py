from rest_framework import serializers
from models import Review


class ReviewSerializer(serializers.ModelSerializer):
    renter = serializers.ReadOnlyField(source='renter.username')

    class Meta:
        model = Review
        fields = ['id', 'renter', 'rent', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'renter', 'created_at']
