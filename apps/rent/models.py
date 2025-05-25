from django.db import models

from apps.rent.choices.room_type import RoomType


class Rent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=170)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    rooms_count = models.PositiveSmallIntegerField()
    room_type = models.CharField(max_length=50, choices=RoomType.choices)