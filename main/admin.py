from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number','bio','avatar')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Banner)
admin.site.register(Info)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Pharma)
admin.site.register(Product)
