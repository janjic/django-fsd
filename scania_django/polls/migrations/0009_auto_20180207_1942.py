# Generated by Django 2.0.2 on 2018-02-07 19:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180207_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 2, 7, 19, 42, 25, 712608, tzinfo=utc), verbose_name='date'),
        ),
    ]
