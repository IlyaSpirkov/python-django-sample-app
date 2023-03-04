from django.contrib.auth import get_user_model

User = get_user_model()


class AccountService:
    __slots__ = ()

    @staticmethod
    def register_new_user(email: str, password: str):
        return User.objects.create_user(email=email, password=password)

    @staticmethod
    def delete_user(user: User):
        user.delete()
