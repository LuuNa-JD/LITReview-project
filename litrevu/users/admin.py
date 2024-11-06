from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserFollows
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'password1', 'password2',
                'is_staff', 'is_active', 'groups', 'user_permissions'
            )
        }),
    )
    search_fields = ('email', 'username')
    ordering = ['email']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserFollows)
