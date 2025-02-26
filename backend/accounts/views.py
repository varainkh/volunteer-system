from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import VolunteerProfile
from .serializers import RegisterSerializer, VolunteerProfileSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class VolunteerProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = VolunteerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.volunteer_profile

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
