from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email',)
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {
            'fields': ('username', 'fullname', 'email', 'password')
        
        }),
        ('date', {
            'fields': ('created_at', 'updated_at',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'fullname', 'email', 'password1', 'password2' )
        }),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return('username', 'created_at', 'updated_at', )
        else:
            return('created_at', 'updated_at', )

admin.site.register(User, UserAdmin)