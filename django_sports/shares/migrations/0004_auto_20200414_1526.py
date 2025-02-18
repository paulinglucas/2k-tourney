# Generated by Django 3.0.2 on 2020-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0003_auto_20200414_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away',
            field=models.CharField(max_length=100, verbose_name='Away Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='awayML',
            field=models.IntegerField(verbose_name='Away Moneyline'),
        ),
        migrations.AlterField(
            model_name='game',
            name='awaySpread',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Away Spread'),
        ),
        migrations.AlterField(
            model_name='game',
            name='didAwaySpread',
            field=models.BooleanField(default=False, verbose_name='Away Covered Spread'),
        ),
        migrations.AlterField(
            model_name='game',
            name='didAwayWin',
            field=models.BooleanField(default=False, verbose_name='Away Team Won'),
        ),
        migrations.AlterField(
            model_name='game',
            name='didHomeSpread',
            field=models.BooleanField(default=False, verbose_name='Home Covered Spread'),
        ),
        migrations.AlterField(
            model_name='game',
            name='didHomeWin',
            field=models.BooleanField(default=False, verbose_name='Home Team Won'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameOver',
            field=models.BooleanField(default=False, editable=False, verbose_name='Game is Over'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameStarted',
            field=models.BooleanField(default=False, verbose_name='Game has Begun'),
        ),
        migrations.AlterField(
            model_name='game',
            name='home',
            field=models.CharField(max_length=100, verbose_name='Home Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='homeML',
            field=models.IntegerField(verbose_name='Home Moneyline'),
        ),
        migrations.AlterField(
            model_name='game',
            name='homeSpread',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Home Spread'),
        ),
        migrations.AlterField(
            model_name='game',
            name='maxToRiskAway',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='maxToRiskHome',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='maxToRiskSpread',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='maxToWin',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10000, verbose_name='Max Amount Someone can Win'),
        ),
        migrations.AlterField(
            model_name='share',
            name='americanOdds',
            field=models.IntegerField(verbose_name='Odds'),
        ),
        migrations.AlterField(
            model_name='share',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Out of Tournament'),
        ),
        migrations.AlterField(
            model_name='share',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hide'),
        ),
        migrations.AlterField(
            model_name='share',
            name='initialAmount',
            field=models.IntegerField(default=50, verbose_name='Amount of Available Shares'),
        ),
        migrations.AlterField(
            model_name='share',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='share',
            name='pricePerShare',
            field=models.CharField(blank=True, editable=False, max_length=100, verbose_name='Price/Share'),
        ),
        migrations.AlterField(
            model_name='share',
            name='seed',
            field=models.IntegerField(verbose_name='Seed'),
        ),
        migrations.AlterField(
            model_name='share',
            name='win',
            field=models.BooleanField(default=False, verbose_name='Winner'),
        ),
    ]
