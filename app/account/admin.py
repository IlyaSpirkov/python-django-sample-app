from django.contrib import admin

from account.models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fk_name = "user"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_active")
    list_filter = ("email", "is_active")
    search_fields = ("email",)
    inlines = (ProfileInline,)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "phone_confirmed")
    list_filter = ("phone_confirmed",)
    search_fields = ("phone", "user__email")
