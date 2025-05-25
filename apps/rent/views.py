from rest_framework import generics, permissions
from .models import Rent
from django.shortcuts import render
#from .permissions import IsOwnerOrReadOnly
from .serializer import RentSerializer


class RentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rent.objects.select_related('owner').all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly ] #IsOwnerOrReadOnly]



