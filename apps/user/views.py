from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from apps.rent.serializer import RentSerializer
from apps.rent.models import Rent
from .serializers import UserRegistrationSerializer, UserSerializer, ChangePasswordSerializer, MyCustomJWTSerializer
from apps.user.owner_permission import IsRentOwnerOrReadOnly

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from apps.user.owner_permission import IsRentOwnerOrReadOnly
import logging
logger = logging.getLogger(__name__)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.prefetch_related('rent_owner')
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class LoginUserAPIView(APIView):
    # queryset = User.objects.prefetch_related('rent_owner')
    serializer_class = MyCustomJWTSerializer
    permission_classes = [AllowAny]


class CurrentUserAPIView(APIView):
    # serializer_class = MyCustomJWTSerializer
    # permission_classes = [IsAuthenticated]

    # def get(self):
    #     return self.request.user
        # print("request", request, request.user, request.data)
        # serializer = UserSerializer(request.user)
        # return Response(serializer.data)

    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"User: {request.user} | Authenticated: {request.user.is_authenticated}")
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateUserAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"old_password": "Wrong password."}, status=400)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully."})
        return Response(serializer.errors, status=400)

class AdminUserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

class RentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated, IsRentOwnerOrReadOnly]