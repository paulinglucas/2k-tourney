# Generated by Django 3.0.2 on 2020-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0002_auto_20200413_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hide'),
        ),
        migrations.AlterField(
            model_name='request',
            name='numShares',
            field=models.IntegerField(verbose_name='Number of Shares Sold'),
        ),
        migrations.AlterField(
            model_name='request',
            name='salePrice',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=10000, verbose_name='Sale Price'),
        ),
    ]
