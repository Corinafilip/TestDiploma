from django.contrib.auth.models import User
from django.db import models

from apps.rent.choices.room_type import RoomType


class Rent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=170)
    price_per_night = models.DecimalField(decimal_places=2, max_digits=6)
    rooms_count = models.PositiveSmallIntegerField()
    room_type = models.CharField(max_length=50, choices=RoomType.choices)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, related_name='rent_owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    score = models.DecimalField(decimal_places=2, max_digits=1)
    reviews = models.PositiveIntegerField(default=0)
