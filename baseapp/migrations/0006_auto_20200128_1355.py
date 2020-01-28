# Generated by Django 2.2.5 on 2020-01-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_auto_20200124_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='car_model',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Марка А/М'),
        ),
        migrations.AddField(
            model_name='driver',
            name='car_number',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Номер А/М'),
        ),
        migrations.AddField(
            model_name='driver',
            name='driver_license',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Номер В/У'),
        ),
        migrations.AddField(
            model_name='driver',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Ставка'),
        ),
    ]