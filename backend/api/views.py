from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PatternSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from .models import Pattern

# create your views here
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PatternListCreateView(generics.ListCreateAPIView):
    # queryset = Patterns.objects.all()
    serializer_class = PatternSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Pattern.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class PatternDeleteView(generics.DestroyAPIView):
    serializer_class = PatternSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Pattern.objects.filter(author=user)

