# Generated by Django 3.0.2 on 2020-04-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('exchanges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to='login.Profile'),
        ),
        migrations.AddField(
            model_name='request',
            name='salePrice',
            field=models.DecimalField(decimal_places=2, default=-1.0, max_digits=10000),
        ),
    ]
