from dataclasses import dataclass
from datetime import date

from django.contrib.auth import get_user_model
from account.models import Profile
from account.services.image_upload import ImageUploader


User = get_user_model()


@dataclass
class UpdateProfileDTO:
    phone: str = ""
    birthday: date | None = None
    address: str = ""
    zip_code: str = ""


class ProfileService:
    __slots__ = ()

    @staticmethod
    def get_user_profile(user: User) -> Profile:
        profile = user.profile
        if profile is None:
            profile = Profile(user=user)
        return profile

    @staticmethod
    def update_profile(user: User, data: UpdateProfileDTO) -> Profile:
        profile = ProfileService().get_user_profile(user)
        profile.phone = data.phone
        profile.birthday = data.birthday
        profile.address = data.address
        profile.zip_code = data.zip_code
        profile.save()
        return profile

    @staticmethod
    def update_avatar(user: User, img) -> Profile:
        profile = ProfileService().get_user_profile(user)
        profile.avatar = ImageUploader().upload_avatar_to_s3(img, user.id)
        profile.save()
        return profile
