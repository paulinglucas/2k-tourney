from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from shares.models import Share, Game
import datetime
from django.utils.timezone import now

class InvestedShareManager(models.Manager):
    def createInvestment(self, user, share, numSharesHeld, boughtAt):
        share = self.create(user=user, share=share,
            numSharesHeld=numSharesHeld, boughtAt=boughtAt)
        return share

class InvestedGameManager(models.Manager):
    def createInvestment(self, user, game, amountUsed, amOdds, oddsAtPurchase, bet):
        share = self.create(user=user, game=game,
            amountUsed=amountUsed, amOdds=amOdds, oddsAtPurchase=oddsAtPurchase, bet=bet)
        return share

# Create your models here.
class InvestedShare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    numSharesHeld = models.IntegerField("Number of Shares Held")
    boughtAt = models.CharField("Price Purchased", max_length=100, blank=True)
    hidden = models.BooleanField("Hide", default=False)
    created = models.DateTimeField(default=now, null=True)

    objects = InvestedShareManager()

    def __str__(self):
        return self.user.profile.first_name + " holds " + str(self.numSharesHeld) + " shares in " + self.share.name

class InvestedGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amountUsed = models.DecimalField("Amount Bet", max_digits=10000, decimal_places=2)
    amOdds = models.IntegerField("Odds")
    oddsAtPurchase = models.FloatField("Decimal Odds")
    # 1=homeML, 2=awayML, 3=homeSpread, 4=awaySpread
    bet = models.IntegerField("Bet Placed")
    hidden = models.BooleanField("Hide", default=False)
    created = models.DateTimeField(default=now, null=True)

    objects = InvestedGameManager()

    def didTheyWin(self):
        win = False
        if self.game.gameOver:
            if self.bet == 1 and self.game.didHomeWin:
                win = True
            elif self.bet == 2 and self.game.didAwayWin:
                win = True
            elif self.bet == 3 and self.game.didHomeSpread:
                win = True
            elif self.bet == 4 and self.game.didAwaySpread:
                win = True
        return win

    def __str__(self):
        return self.user.profile.first_name + " bet " + str(self.amountUsed) + " on " + self.game.home + " vs " + self.game.away
