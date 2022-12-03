from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from api.models import Event, Note, Achievement, Advertisement, User


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Заметки"""
    list_display = ("type",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """События"""
    list_display = ("header",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Достижения"""
    list_display = ("name",)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = ("header",)


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ('achievements_received',)
    fieldsets = (
        (None, {'fields': ('email',  'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name', 'achievements_received')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )


admin.site.register(User, CustomUserAdmin,)
