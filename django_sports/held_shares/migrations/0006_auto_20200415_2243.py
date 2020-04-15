# Generated by Django 3.0.2 on 2020-04-15 22:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('held_shares', '0005_auto_20200415_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investedgame',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 22, 43, 39, 762252, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='investedshare',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 22, 43, 39, 762252, tzinfo=utc)),
        ),
    ]
