# Generated by Django 3.0.2 on 2020-04-15 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('held_shares', '0006_auto_20200415_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investedgame',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='investedshare',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
