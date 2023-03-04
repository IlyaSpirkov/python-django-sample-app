from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthService:
    __slots__ = ()

    @staticmethod
    def blacklist_user_tokens(user: User):
        RefreshToken.for_user(user).blacklist()
