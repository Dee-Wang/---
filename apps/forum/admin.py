from django.contrib import admin

from .models import ForumPost, Board


# 板块后台管理
class BoardAdmin(admin.ModelAdmin):
    list_display = ('board_creator','board_name','add_time')
    search_fields = ['board_name',]
    list_filter = ('board_creator', )


# 帖子后台管理
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('forum_title','forum_content','forum_creator','board','updated_time', 'recommend_num')
    search_fields = ['forum_title',]
    list_filter = ('board', )


# 将上面的内容注册到admin中
admin.site.register(ForumPost, ForumPostAdmin)
admin.site.register(Board, BoardAdmin)
