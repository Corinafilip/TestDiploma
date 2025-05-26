# apps/rent/models/review.py

from django.db import models
from django.conf import settings
from apps.rent.models import Rent


class Review(models.Model):
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.PositiveSmallIntegerField()  # e.g., 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('renter', 'rent')  # prevent duplicate reviews

    def __str__(self):
        return f"Review by {self.renter} on {self.rent}"
