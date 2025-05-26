from rest_framework import permissions
from rest_framework.permissions import BasePermission
from apps.bookings.models import Booking

class IsRentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

#restrict updates only to renters or owners,  create a custom permission:
class IsRenterAndOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.owner and
            request.user.role == "RENTER"
        )

class HasCompletedBooking(BasePermission):
    """
    Allow only users who completed a booking to leave a review.
    """

    def has_permission(self, request, view):
        if request.method != 'POST':
            return True

        rent_id = request.data.get('rent')
        if not rent_id:
            return False

        return Booking.objects.filter(
            renter=request.user,
            title_id=rent_id,
            is_cancelled=False,
            check_out__lt=request.timestamp  # only after checkout
        ).exists()

