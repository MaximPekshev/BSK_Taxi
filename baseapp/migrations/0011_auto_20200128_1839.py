# Generated by Django 2.2.5 on 2020-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0010_auto_20200128_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='working_day',
            name='date',
            field=models.DateField(verbose_name='Дата рабочего дня'),
        ),
    ]