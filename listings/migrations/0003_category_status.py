# Generated by Django 3.2.6 on 2021-08-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210804_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='نمایش داده شود'),
        ),
    ]
