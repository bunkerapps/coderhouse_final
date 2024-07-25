from django.contrib import admin
from django.utils.html import format_html
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'photo_tag')

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return '-'
    photo_tag.short_description = 'Photo'

admin.site.register(User, UserAdmin)