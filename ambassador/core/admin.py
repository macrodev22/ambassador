from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Order, Product, User, Link


# Register your models here.

class SuperUser(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_ambassador')

    # Which fields are visible and modifiable in admin interface
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_ambassador')})
    )

    # Which fields are shown when adding a user in admin site
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields' : ('email', 'password', 'password2', 'is_staff', 'is_ambassador', 'is_active')}),

    )
    ordering = ['id']



admin.site.register(User, SuperUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Link)