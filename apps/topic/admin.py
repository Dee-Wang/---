from django.contrib import admin

from .models import FoodTopic

# 食物详情后台管理
class FoodTopicAdmin(admin.ModelAdmin):
    list_display = ('title','cover_image','description','total_collects','tags', 'add_time')
    search_fields = ['title',]
    list_filter = ('tags', )


# 将上面的内容注册到admin中
admin.site.register(FoodTopic, FoodTopicAdmin)