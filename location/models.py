from django.db import models

# Create your models here.
"""创建居住地信息的数据表"""


# 所在省份
class Province(models.Model):
    province_name = models.CharField(max_length=32, verbose_name='省份名称', default=' ')

    def __str__(self):
        return self.province_name

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = '省份'


# 所在城市
class City(models.Model):
    city_name = models.CharField(max_length=32, verbose_name='城市名称', default=' ')
    province = models.ForeignKey(Province, verbose_name='省份')

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'


# 具体地点
class Store(models.Model):
    store_name = models.CharField(max_length=64, verbose_name='店铺名称', default=' ')
    address = models.CharField(max_length=128, verbose_name="具体地址", null=True, blank=True)
    city = models.ForeignKey(City, verbose_name='所在城市')

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = "店铺"
        verbose_name_plural = verbose_name