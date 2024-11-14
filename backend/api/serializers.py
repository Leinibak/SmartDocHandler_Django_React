from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pattern

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
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
        extra_kwargs={"author":{"read_only":True}}

    # def validate_category(self, value):
    #     """category 필드 유효성 검사"""
    #     if value not in ["invoice", "credit"]:
    #         raise serializers.ValidationError("Category must be either 'invoice' or 'credit'.")
    #     return value

    # def validate_region(self, value):
    #     """region 필드 유효성 검사"""
    #     if value not in ["domestic", "foreign"]:
    #         raise serializers.ValidationError("Region must be either 'domestic' or 'foreign'.")
    #     return value

    # def create(self, validated_data):
    #     """패턴 생성 시 author 필드를 현재 사용자로 자동 설정"""
    #     validated_data["author"] = self.context["request"].user
    #     return super().create(validated_data)

