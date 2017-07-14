from django.contrib import admin

from .models import UserWantEat, UserHaveAte, UserCollectTopic, UserRecommendForum


class UserWantEatAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'add_time')
    search_fields = ['user', 'food']
    list_filter = ('user', 'food')


class UserHaveAteAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'add_time')
    search_fields = ['user', 'food']
    list_filter = ('user', 'food')


class UserCollectTopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'add_time')
    search_fields = ['user', 'topic']
    list_filter = ('user', 'topic')


class UserRecommendForumAdmin(admin.ModelAdmin):
    list_display = ('user', 'forum', 'add_time')
    search_fields = ['user', 'forum']
    list_filter = ('user', 'forum')


class FoodInTopicAdmin(admin.ModelAdmin):
    list_display = ('food', 'topic', 'add_time')
    search_fields = ['food', 'topic']
    list_filter = ('food', 'topic')



# 将上面的内容注册到admin中
admin.site.register(UserWantEat, UserWantEatAdmin)
admin.site.register(UserHaveAte, UserHaveAteAdmin)
admin.site.register(UserCollectTopic, UserCollectTopicAdmin)
admin.site.register(UserRecommendForum, UserRecommendForumAdmin)
# admin.site.register(FoodInTopic, FoodInTopicAdmin)
