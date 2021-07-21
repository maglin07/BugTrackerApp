from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User role:",
            {
                'fields': (
                    'displayname',
                    'age',
                    'homepage'
                ),
            },
            ),
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
