from datetime import timedelta
from django.utils import timezone

def can_cancel(booking):
    return timezone.now() < booking.check_in - timedelta(days=3)