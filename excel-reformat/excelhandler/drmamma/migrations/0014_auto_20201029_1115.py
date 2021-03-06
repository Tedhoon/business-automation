# Generated by Django 3.0.8 on 2020-10-29 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmamma', '0013_auto_20201028_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe24temp',
            name='store_code',
            field=models.TextField(blank=True, null=True, verbose_name='발주처 코드'),
        ),
        migrations.AlterField(
            model_name='cafe24',
            name='extract_day',
            field=models.CharField(default=datetime.datetime(2020, 10, 29, 11, 15, 3, 958797), max_length=10, verbose_name='출고일자'),
        ),
        migrations.AlterField(
            model_name='deliveryexcel',
            name='uploaded_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 29, 11, 15, 3, 959795), verbose_name='업로드 날짜'),
        ),
    ]
