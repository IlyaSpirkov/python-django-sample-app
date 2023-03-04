from rest_framework import serializers

from account.models import Profile
from account.api.profile.validators import validate_image


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ("id", "user", "phone_confirmed", "avatar")
        extra_kwargs = {"avatar": {"read_only": True}}


class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.FileField(validators=[validate_image], required=False)
