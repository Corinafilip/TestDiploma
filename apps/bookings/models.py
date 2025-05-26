from django.db import models
from django.conf import settings
from apps.rent.models import Rent


class Booking(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()

    # Redundant fields for snapshot/history (in case Rent is updated or deleted)
    property_address = models.CharField(max_length=170)
    room_type = models.CharField(max_length=50)

    guests = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    paid = models.BooleanField(default=False, null=True, blank=True)

    is_cancelled = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)


    renter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings_made'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings_received'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'booking'

    def __str__(self):
        return f"{self.rent.title} - {self.renter.username}"
