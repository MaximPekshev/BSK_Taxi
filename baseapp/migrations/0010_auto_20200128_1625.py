# Generated by Django 2.2.5 on 2020-01-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_auto_20200128_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='working_day',
            name='slug',
            field=models.SlugField(blank=True, max_length=10, verbose_name='Url'),
        ),
    ]
