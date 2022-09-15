from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role, Department

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields' : ('role', 'department', 'years', 'email')}),
    )
    fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields' : ('role', 'department', 'years', 'email')}),
    )
    list_display = [
        'username', 'email', 'role',
        'years', 'department', 'is_staff'
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Department)