from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import UserProfile, UserSetting, EmailVerifyRecord


class UserSettingAdmin(admin.TabularInline):
    model = UserSetting


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        ('个人信息', {'fields': ('username', 'email', 'password', 'nickname', 'location', 'introduction', 'gender', 'birthday', 'phone_num', 'avatar', 'following')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('登录信息', {'fields': ('date_joined', 'last_login',)}),
    )
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('date_joined',)

    inlines = [
        UserSettingAdmin
    ]


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'send_type', 'code')
    search_fields = ['email', 'send_type']
    list_filter = ('email', 'send_type')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)