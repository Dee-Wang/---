from django.contrib import admin

from .models import UserProfile, EmailVerifyRecord

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','nickname', 'birthday', 'gender', 'location', 'phone_num', 'image')
    search_fields = ('username', 'email','nickname', 'location', 'phone_num')
    list_filter = ('username', 'email','nickname', 'location', 'phone_num', 'gender')


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'send_type', 'code')
    search_fields = ['email', 'send_type']
    list_filter = ('email', 'send_type')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)