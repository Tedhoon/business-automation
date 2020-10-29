# Generated by Django 3.0.8 on 2020-10-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmamma', '0018_remove_cafe24temp_standard_for_gift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naverfarmtemp',
            name='discount_coupon',
        ),
        migrations.RemoveField(
            model_name='naverfarmtemp',
            name='discount_product',
        ),
        migrations.RemoveField(
            model_name='naverfarmtemp',
            name='standard_for_gift',
        ),
        migrations.RemoveField(
            model_name='naverfarmtemp',
            name='used_reserves',
        ),
        migrations.AddField(
            model_name='naverfarmtemp',
            name='order_price',
            field=models.TextField(blank=True, null=True, verbose_name='배송비 합계'),
        ),
    ]