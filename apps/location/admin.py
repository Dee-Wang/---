from django.contrib import admin

from .models import Province, City, Store


class CityAdmin(admin.TabularInline):
    model = City


class ProvinceAdmin(admin.ModelAdmin):
    model = Province

    inlines = [
        CityAdmin,
    ]


# 将上面的内容注册到admin中
admin.site.register(Province, ProvinceAdmin)

