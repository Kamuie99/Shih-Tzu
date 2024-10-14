from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('liked_movies', 'following')}),
    )

    filter_horizontal = ('liked_movies', 'following',)

admin.site.register(User, CustomUserAdmin)