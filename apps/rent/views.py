from rest_framework import generics, permissions
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from .models import Rent
from django.shortcuts import render
from .permissions import IsRentOwnerOrReadOnly
from .serializer import RentSerializer
from django.db import models
from apps.user.owner_permission import IsRentOwnerOrReadOnly


class RentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rent.objects.select_related('owner').all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [IsRentOwnerOrReadOnly]

class RentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsRentOwnerOrReadOnly]

class RentListAPIView(ListAPIView):
    queryset = Rent.objects.all()  # uses filtered manager
    serializer_class = RentSerializer

