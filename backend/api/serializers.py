from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patterns

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class PatternsSerializer(serializers.ModelSerializer):
    # author는 자동으로 현재 로그인된 사용자가 설정되므로 읽기 전용 필드로 설정합니다.
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Patterns
        fields = [
            "id",
            "customer",
            "title",
            "category",
            "region",
            "pattern",
            "created_at",
            "author",
        ]

    def validate_category(self, value):
        """category 필드 유효성 검사"""
        if value not in ["invoice", "credit"]:
            raise serializers.ValidationError("Category must be either 'invoice' or 'credit'.")
        return value

    def validate_region(self, value):
        """region 필드 유효성 검사"""
        if value not in ["domestic", "foreign"]:
            raise serializers.ValidationError("Region must be either 'domestic' or 'foreign'.")
        return value

    def create(self, validated_data):
        """패턴 생성 시 author 필드를 현재 사용자로 자동 설정"""
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

