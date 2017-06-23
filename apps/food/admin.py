from django.contrib import admin

from .models import FoodCategory, Food


# 食物种类后台管理
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ['category_name',]
    list_filter = ('category_name',)


# 食物详情后台管理
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title','food_name','description','cover_image','rating','users_wta', 'users_ate','link','category', 'user','add_time','tags')
    search_fields = ['title','food_name','category', 'user','tags']
    list_filter = ('title','food_name','category', 'user','tags')



# 将上面的内容注册到admin中
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)