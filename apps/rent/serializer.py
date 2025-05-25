from rest_framework import serializers
from .models import Rent

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']
