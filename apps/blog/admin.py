from django.contrib import admin

from .models import Blog


# 后台博文管理
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_user', 'blog_content','created_time' )
    search_fields = ['blog_title', 'blog_user', 'blog_content',]
    list_filter = ('blog_title', 'blog_user', 'blog_content',)


# 将上面的内容注册到admin中
admin.site.register(Blog, BlogAdmin)