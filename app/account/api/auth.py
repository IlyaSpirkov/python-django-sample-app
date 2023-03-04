from drf_spectacular.utils import extend_schema, inline_serializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions, response, serializers
from rest_framework.views import APIView

from account.services.auth import AuthService

User = get_user_model()


@extend_schema(
    tags=["auth"],
    request=TokenObtainPairSerializer,
    responses={200: inline_serializer("Tokens", {"access": serializers.CharField(), "refresh": serializers.CharField()})},
)
class LoginApi(TokenObtainPairView):
    queryset = User.objects.all()


@extend_schema(
    tags=["auth"],
    request=TokenRefreshSerializer,
    responses={200: inline_serializer("AccessToken", {"access": serializers.CharField()})},
)
class RefreshTokenApi(TokenRefreshView):
    ...


@extend_schema(
    tags=["auth"],
    responses={200: None},
)
class LogoutApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        AuthService.blacklist_user_tokens(request.user)
        return response.Response()
