from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, DetailChangeForm
from .models import CustomUser

"""class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm()
    form = DetailChangeForm()
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("emial", "is_staff", "is_active")
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classses': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'is_staff', 'is_active', 'is_superuser',
                'groups', 'user_permissions',
            )
        }),
    )
    search_fields = ('email',)
    ordering = ('email')"""

# Registering model
admin.site.register(CustomUser)
#admin.site.register(CustomUserAdmin)
