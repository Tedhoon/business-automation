# Generated by Django 3.0.8 on 2021-03-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drmamma', '0022_auto_20210323_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='max_range',
            field=models.PositiveIntegerField(null=True, verbose_name='최대 금액(~원 전까지)'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='min_range',
            field=models.PositiveIntegerField(null=True, verbose_name='최소 금액(~원 부터)'),
        ),
    ]