# Generated by Django 3.0.2 on 2020-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10000, verbose_name='Current Profit'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Last Name'),
        ),
    ]
