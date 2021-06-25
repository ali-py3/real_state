from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING,verbose_name="مشاوره املک")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    address = models.CharField(max_length=200, verbose_name="ادرس")
    city = models.CharField(max_length=100, verbose_name="شهر")
    state = models.CharField(max_length=100, verbose_name="دولت")
    zipcode = models.CharField(max_length=20, verbose_name="کد پستی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    bedrooms = models.IntegerField(verbose_name="اتاق خواب")
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="سرویس یهداشتی")
    garage = models.IntegerField(default=0, verbose_name="پارکینگ")
    sqft = models.IntegerField(verbose_name="فوت مربع")
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="متراژ کلی")
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="تصویر اصلی")
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر اول")
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر دوم")
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر سوم")
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر چهارم")
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر پنجم")
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="تصویر ششم")
    is_published = models.BooleanField(default=True, verbose_name="نشان دادن")
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name="تاریخ نمایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ملک ها"
        verbose_name = "ملک ها"