from rest_framework import permissions

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