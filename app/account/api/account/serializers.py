from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation as validators

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def validate_password(self, value):
        validators.validate_password(password=value)
        return value
