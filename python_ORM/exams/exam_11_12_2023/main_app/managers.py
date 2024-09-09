from django.db import models
from django.db.models import Count


class TennisPlayerManager(models.Manager):
    def get_tennis_players_by_wins_count(self):
        return self.annotate(player_wins=Count('matches_won')).order_by('-player_wins', 'full_name')
