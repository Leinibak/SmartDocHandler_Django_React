from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PatternsSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from .models import Patterns 

# create your views here
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PatternListCreateView(generics.ListCreateAPIView):
    """
    패턴을 목록화하고 새 패턴을 생성합니다.
    관리자만 접근 가능합니다.
    """
    queryset = Patterns.objects.all()
    serializer_class = PatternsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        # 요청한 사용자(관리자)를 author로 설정
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class PatternRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    특정 패턴을 조회하거나 삭제합니다.
    관리자만 접근 가능합니다.
    """
    queryset = Patterns.objects.all()
    serializer_class = PatternsSerializer
    permission_classes = [IsAdminUser]
 
