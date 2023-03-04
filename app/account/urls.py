from django.urls import path

from account.api.account.api import RegisterApi, DeleteAccountApi
from account.api.auth import LoginApi, LogoutApi, RefreshTokenApi
from account.api.profile.api import AvatarApi, ProfileApi


urlpatterns = [
    path("account/register/", RegisterApi.as_view(), name="register"),
    path("account/", DeleteAccountApi.as_view(), name="delete_account"),

    path("auth/login/", LoginApi.as_view(), name="login"),
    path("auth/logout/", LogoutApi.as_view(), name="logout"),
    path("auth/refresh/", RefreshTokenApi.as_view(), name="refresh"),

    path("profile/", ProfileApi.as_view(), name="profile"),
    path("profile/avatar", AvatarApi.as_view(), name="avatar"),

]
