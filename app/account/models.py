from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import CustomUserManager


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True, null=True)
    phone = PhoneNumberField(unique=True, max_length=20, null=True, blank=True)
    phone_confirmed = models.BooleanField(default=False)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "пользовательский профиль"
        verbose_name_plural = "пользовательские профили"

    def __str__(self):
        return str(self.user)
