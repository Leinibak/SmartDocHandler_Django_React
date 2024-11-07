from django.db import models
from django.contrib.auth.models import User

class Patterns(models.Model):
    # 고객사 이름
    customer = models.CharField(max_length=100)

    # 패턴 이름이나 제목
    title = models.CharField(max_length=100)

    # Invoice/Credit 유형 선택
    CATEGORY_CHOICES = [
        ('invoice', 'Invoice'),
        ('credit', 'Credit'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    # Domestic/Foreign 여부 선택
    REGION_CHOICES = [
        ('domestic', 'Domestic'),
        ('foreign', 'Foreign'),
    ]
    region = models.CharField(max_length=10, choices=REGION_CHOICES)

    # 패턴 내용
    pattern = models.TextField()

    # 패턴 생성 시간 자동 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # 작성자와의 외래키 연결 (관리자만 접근 가능)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patterns")

    def __str__(self):
        return f"{self.customer} - {self.category} ({self.region})"

    # 관리자만 접근 가능하도록 하기 위한 설정
    def save(self, *args, **kwargs):
        if not self.author.is_staff:
            raise PermissionError("Only admins can create or modify patterns.")
        super().save(*args, **kwargs)
