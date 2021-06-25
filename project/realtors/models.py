from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="تصویر")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    email = models.CharField(max_length=50, verbose_name="ایمیل")
    is_mvp = models.BooleanField(default=False, verbose_name="نمایش")
    hire_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "مشاورین املاک"
        verbose_name = "مشاوره املاک"