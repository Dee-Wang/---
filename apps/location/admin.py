from django.contrib import admin

from django.contrib import admin

from .models import Province, City, Store


# 省份后台管理的部分
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province_name', )
    search_fields = ['province_name', ]
    list_filter = ('province_name', )


# 城市后台管理部分
class CityAdmin(admin.ModelAdmin):
    list_display = ('province', 'city_name')
    search_fields = ['province', 'city_name']
    list_filter = ('province', 'city_name')


# 商店后台管理部分
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name','city','address',)
    search_fields = ['store_name', 'city','address',]
    list_filter = ('store_name', 'city','address',)


# 将上面的内容注册到admin中
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Store, StoreAdmin)
