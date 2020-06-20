from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display    = ('get_username','is_available','available_since')
    # search_fields   = (),
    # list_editable   = (),
    # readonly_fields = (),
    # filter_horizntal= (),
    list_filter     = ('available_since','is_available')
    # fieldsets       = (),
    pass
# admin.site.register(Profile)
admin.site.register(Profile,ProfileAdmin)
