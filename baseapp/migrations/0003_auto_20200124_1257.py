# Generated by Django 2.2.5 on 2020-01-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_auto_20200124_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='slug',
            field=models.SlugField(blank=True, max_length=10, null=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='working_day',
            name='slug',
            field=models.SlugField(blank=True, max_length=10, null=True, verbose_name='Url'),
        ),
    ]