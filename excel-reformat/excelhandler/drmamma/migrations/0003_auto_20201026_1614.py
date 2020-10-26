# Generated by Django 3.0.8 on 2020-10-26 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmamma', '0002_auto_20201026_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe24',
            name='extract_day',
            field=models.CharField(default=datetime.datetime(2020, 10, 26, 16, 14, 10, 454178), max_length=10, verbose_name='출고일자'),
        ),
        migrations.AlterField(
            model_name='deliveryexcel',
            name='excel_file',
            field=models.FileField(upload_to='excel', verbose_name='송장 엑셀'),
        ),
        migrations.AlterField(
            model_name='deliveryexcel',
            name='uploaded_at',
            field=models.DateField(auto_now=True, verbose_name='업로드 날짜'),
        ),
    ]
