from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from archiver.models import ArchiverApp, ArchiverProfile

class ArchiverProfileInline(admin.StackedInline):
    model = ArchiverProfile
    can_delete = False
    verbose_name_plural = 'archivee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ArchiverProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(ArchiverApp)
