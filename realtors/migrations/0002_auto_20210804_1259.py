# Generated by Django 3.2.6 on 2021-08-04 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realtor',
            options={'verbose_name': 'مشاوره املاک', 'verbose_name_plural': 'مشاورین املاک'},
        ),
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=50, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False, verbose_name='نمایش'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(max_length=200, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='تصویر'),
        ),
    ]
