from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'full_name', 'is_staff', 'is_superuser')
    list_editable = ('is_staff', 'is_superuser')