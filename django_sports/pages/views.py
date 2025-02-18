from django.shortcuts import render
from shares.models import Share, Game
from held_shares.models import InvestedShare, InvestedGame
from exchanges.models import Request
from decimal import Decimal
from odds_update.views import calculateProfit

def checkIfHidden():
	for share in InvestedShare.objects.filter(hidden=True):
		if not share.share.hidden:
			share.hidden = False
			share.save()
	for game in InvestedGame.objects.filter(hidden=True):
		if not game.game.gameOver:
			game.hidden = False
			game.save()

def checkRequests():
	for req in Request.objects.all():
		if req.inv_share.hidden:
			req.hidden = True
			req.save()

def checkIfBetsWon():
	for share in Share.objects.exclude(hidden=True):
		if share.done == True or share.win == True:
			share.hidden = True
			share.save()
	for share in InvestedShare.objects.exclude(hidden=True):
		if share.share.hidden:
			share.hidden = True
			share.save()

def checkIfGamesWon():
	for game in Game.objects.exclude(gameOver=True):
		if (game.gameOver == False) and (game.didHomeWin or game.didAwayWin or game.didHomeSpread or game.didAwaySpread):
			game.gameOver = True
			game.save()
	for game in InvestedGame.objects.exclude(hidden=True):
		if game.game.gameOver:
			game.hidden = True
			game.save()

def home_view(request):
	shares = Share.objects.exclude(done=True)
	active_seeds = []
	checkIfBetsWon()
	checkIfGamesWon()

	for share in shares:
		if not any(element[0] == share.seed for element in active_seeds):
			element = (share.seed, Share.objects.filter(seed=share.seed).exclude(hidden=True))
			active_seeds.append(element)
	active_seeds = sorted(active_seeds, key=lambda x: x[0])

	context = {
		'shares': shares,
		'seeds': active_seeds
	}
	return render(request, 'index.html', context)

def my_shares_view(request):
	checkIfHidden()
	checkRequests()
	if not request.user.is_anonymous:
		calculateProfit(request.user)
		current_profit = request.user.profile.current_profit
		shares = InvestedShare.objects.filter(user=request.user).exclude(hidden=True)
		game_shares = InvestedGame.objects.filter(user=request.user).exclude(hidden=True)
		my_requests = Request.objects.exclude(sender=request.user.profile).exclude(hidden=True)
		my_sells = Request.objects.filter(sender=request.user.profile).exclude(hidden=True)

	context = {
		'profit': current_profit,
		'my_shares': shares,
		'game_shares': game_shares,
		'my_requests': my_requests,
		'my_sells': my_sells
	}
	return render(request, 'my_shares.html', context)


def games_view(request):
	games = Game.objects.exclude(gameStarted=True)
	context = {
		'games': games
	}
	return render(request, 'games.html', context)
