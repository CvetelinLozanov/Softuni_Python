import os
import django
from django.db.models import Q, F, Min, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import House, Dragon, Quest


# Create queries within functions
def get_houses(search_string=None):
    # if search_string is None:
    #     return "No houses match your search."

    if not search_string:
        return "No houses match your search."

    query = Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)
    houses = (House.objects
              .filter(query)
              .order_by('-wins', 'name'))

    if not houses:
        return "No houses match your search."

    return '\n'.join(f"House: {h.name}, wins: {h.wins}, motto: {h.motto if h.motto else 'N/A'}" for h in houses)


def get_most_dangerous_house():
    most_dangerous_house = House.objects.get_houses_by_dragons_count().first()

    if not most_dangerous_house or most_dangerous_house.count_of_dragons == 0:
        return "No relevant data."

    return (f"The most dangerous house is the House of {most_dangerous_house.name} with "
            f"{most_dangerous_house.count_of_dragons} dragons. Currently "
            f"{'ruling' if most_dangerous_house.is_ruling else 'not ruling'} the kingdom.")


def get_most_powerful_dragon():
    most_powerful_dragon = (Dragon.objects
                            .filter(is_healthy=True)
                            .order_by('-power', 'name')
                            .first())

    if not most_powerful_dragon:
        return "No relevant data."

    power = f"{most_powerful_dragon.power:.1f}"
    return (f"The most powerful healthy dragon is {most_powerful_dragon.name} with a power level of {power},"
            f" breath type {most_powerful_dragon.breath}, and {most_powerful_dragon.wins} wins,"
            f" coming from the house of {most_powerful_dragon.house.name}."
            f" Currently participating in {most_powerful_dragon.quests.count()} quests.")


def update_dragons_data():
    injured_dragons = Dragon.objects.filter(is_healthy=False, power__gt=1)

    num_of_updated_dragons = (injured_dragons
                              .update(power=F('power') - 0.1, is_healthy=True)
                              )

    if num_of_updated_dragons == 0:
        return "No changes in dragons data."

    min_power = Dragon.objects.aggregate(min_power=Min('power'))['min_power']

    return (f"The data for {num_of_updated_dragons} dragon/s has been changed."
            f" The minimum power level among all dragons is {min_power:.1f}")


def get_earliest_quest():
    quest = Quest.objects.order_by('start_time').first()

    if quest is None:
        return "No relevant data."

    start_time = quest.start_time
    day = start_time.day
    month = start_time.month
    year = start_time.year

    dragons = quest.dragons.order_by('-power', 'name')
    dragon_names_str = "*".join([dragon.name for dragon in dragons])

    avg_power_level = dragons.aggregate(Avg('power'))['power__avg']
    avg_power_level = f"{avg_power_level:.2f}" if avg_power_level else "0.00"

    return (
        f"The earliest quest is: {quest.name}, code: {quest.code}, "
        f"start date: {day}.{month}.{year}, host: {quest.host.name}. "
        f"Dragons: {dragon_names_str}. Average dragons power level: {avg_power_level}")


def announce_quest_winner(quest_code):
    quest = Quest.objects.filter(code=quest_code).first()

    if not quest:
        return "No such quest."

    winner_dragon = quest.dragons.order_by('-power', 'name').first()

    winner_dragon.wins += 1
    winner_dragon.save()

    winner_house = winner_dragon.house
    winner_house.wins += 1
    winner_house.save()

    quest_name = quest.name
    quest_reward = quest.reward
    quest.delete()

    return (f"The quest: {quest_name} has been won by dragon {winner_dragon.name} "
            f"from house {winner_house.name}. The number of wins has been updated as follows: "
            f"{winner_dragon.wins} total wins for the dragon and {winner_house.wins} total wins for the house. "
            f"The house was awarded with {quest_reward:.2f} coins.")


print(announce_quest_winner('BoW#'))



