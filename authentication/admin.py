from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# admin.site.register(CustomUser, UserAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('first_name', 'last_name', 'middle_name', 'email', 'created_at')

    fields = ('first_name', 'last_name', 'middle_name', ('email', 'role'), 'password')
