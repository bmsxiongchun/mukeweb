# Generated by Django 2.1 on 2018-11-22 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181122_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 22, 10, 22, 42, 263598), verbose_name='添加时间'),
        ),
    ]
