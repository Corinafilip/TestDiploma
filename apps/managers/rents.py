from django.db import models

class RentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Rent(models.Model):
    ...
    is_deleted = models.BooleanField(default=False)

    objects = RentManager()  # soft-deletion-aware manager
    all_objects = models.Manager()  #  to access everything, including deleted