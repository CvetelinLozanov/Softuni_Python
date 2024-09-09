import os
import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions
def get_tennis_players(search_name=None, search_country=None) -> str:
    tennis_players = ''

    if search_name is not None and search_country is not None:
        tennis_players = (TennisPlayer.objects
                          .filter(full_name__icontains=search_name, country__icontains=search_country)
                          .order_by('ranking')
                          .values('full_name', 'country', 'ranking'))

    elif search_name is None and search_country is not None:
        tennis_players = (TennisPlayer.objects.filter(country__icontains=search_country)
                          .order_by('ranking')
                          .values('full_name', 'country', 'ranking'))

    elif search_name is not None and search_country is None:
        tennis_players = (TennisPlayer.objects.filter(full_name__icontains=search_name)
                          .order_by('ranking')
                          .values('full_name', 'country', 'ranking'))

    return '\n'.join(f"Tennis Player: {p['full_name']}, country: {p['country']}, ranking: {p['ranking']}"
                     for p in tennis_players) if tennis_players != '' else tennis_players


def get_top_tennis_player():
    player_with_most_wins = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if not player_with_most_wins:
        return ''

    return f"Top Tennis Player: {player_with_most_wins.full_name} with {player_with_most_wins.player_wins} wins."


def get_tennis_player_by_matches_count():
    player_with_most_matches = (TennisPlayer.objects.annotate(matches_played=Count('matches'))
                                .order_by('-matches_played', 'ranking').first())

    if player_with_most_matches and player_with_most_matches.matches_played:
        return (f"Tennis Player: {player_with_most_matches.full_name} with {player_with_most_matches.matches_played} "
                f"matches played.")

    return ''


def get_tournaments_by_surface_type(surface=None):
    tournaments = (Tournament.objects.annotate(matches_count=Count('matches'))
                   .filter(surface_type__icontains=surface)
                   .order_by('-start_date'))

    if not tournaments:
        return ""

    return '\n'.join(f"Tournament: {t.name}, start date: {t.start_date},"
                     f" matches: {t.matches_count}" for t in tournaments)


def get_latest_match_info():
    latest_match = (Match.objects
                    .prefetch_related('players')
                    .select_related('tournament', 'winner')
                    .order_by('-date_played', '-id').first())

    if not latest_match:
        return ''

    player_1_name = latest_match.players.all().order_by('full_name')[0].full_name
    player_2_name = latest_match.players.all().order_by('full_name')[1].full_name
    winner_name = latest_match.winner if latest_match.winner is not None else 'TBA'

    return (f'Latest match played on: {latest_match.date_played}, tournament: {latest_match.tournament.name},'
            f' score: {latest_match.score},'
            f' players: {player_1_name} vs {player_2_name},'
            f' winner: {winner_name}, summary: {latest_match.summary}')


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    match_info = (Match.objects.select_related('tournament', 'winner')
                  .filter(tournament__name=tournament_name)
                  .order_by('-date_played'))

    if not match_info or len(match_info) == 0:
        return "No matches found."

    result = []

    for m in match_info:
        match_winner = m.winner if m.winner is not None else 'TBA'
        match_date = m.date_played
        result.append(f'Match played on: {match_date}, score: {m.score}, winner: {match_winner}')

    return '\n'.join(result)


print(get_tournaments_by_surface_type('gr'))