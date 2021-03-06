# Generated by Django 3.0.8 on 2020-10-28 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmamma', '0005_auto_20201028_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_5',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_12',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_14',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_9',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_1',
            new_name='order_pk',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_7',
            new_name='phone_num',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_6',
            new_name='post_num',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_13',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_11',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_10',
            new_name='product_num',
        ),
        migrations.RenameField(
            model_name='cafe24temp',
            old_name='cf_4',
            new_name='receiver',
        ),
        migrations.RemoveField(
            model_name='cafe24temp',
            name='cf_2',
        ),
        migrations.RemoveField(
            model_name='cafe24temp',
            name='cf_3',
        ),
        migrations.RemoveField(
            model_name='cafe24temp',
            name='cf_8',
        ),
        migrations.AddField(
            model_name='cafe24temp',
            name='phone_num2',
            field=models.TextField(blank=True, null=True, verbose_name='수령인 전화번호'),
        ),
        migrations.AddField(
            model_name='cafe24temp',
            name='product_order_num',
            field=models.TextField(blank=True, null=True, verbose_name='품목별 주문번호'),
        ),
        migrations.AddField(
            model_name='cafe24temp',
            name='total_price',
            field=models.TextField(blank=True, null=True, verbose_name='총 주문 금액'),
        ),
        migrations.AlterField(
            model_name='cafe24',
            name='extract_day',
            field=models.CharField(default=datetime.datetime(2020, 10, 28, 13, 47, 59, 186356), max_length=10, verbose_name='출고일자'),
        ),
        migrations.AlterField(
            model_name='deliveryexcel',
            name='uploaded_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 28, 13, 47, 59, 187353), verbose_name='업로드 날짜'),
        ),
    ]
