import os
import django
from django.db.models import Q, Count, Sum, F, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
# Create queries within functions


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts:
        return ''

    result = []

    for a in astronauts:
        status = 'Active' if a.is_active else 'Inactive'
        result.append(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}")

    return '\n'.join(result)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not top_astronaut or top_astronaut.missions_count == 0:
        return 'No data.'

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


def get_top_commander():
    top_commander = (Astronaut.objects
                     .annotate(num_of_commanded_missions=Count('mission_commander'))
                     .order_by('-num_of_commanded_missions', 'phone_number')
                     .first())

    if not top_commander or top_commander.num_of_commanded_missions == 0:
        return 'No data.'

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_commanded_missions} commanded missions."


def get_last_completed_mission():
    mission = (Mission.objects.filter(status='Completed').select_related('commander', 'spacecraft')
                              .prefetch_related('astronauts')
                              .order_by('-launch_date').first())

    if not mission:
        return 'No data.'

    commander_name = mission.commander.name if mission.commander else "TBA"
    astronauts = mission.astronauts.all().order_by('name')
    astronaut_names = ", ".join(astronaut.name for astronaut in astronauts)
    spacecraft_name = mission.spacecraft.name
    total_spacewalks = astronauts.aggregate(total=Sum('spacewalks'))['total']

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronaut_names}. "
            f"Spacecraft: {spacecraft_name}. "
            f"Total spacewalks: {total_spacewalks}.")

    # mission_astronauts = last_completed_mission.astronauts.all().order_by('name')
    # commander = last_completed_mission.commander.name if last_completed_mission.commander else 'TBA'
    # total_spacewalks = mission_astronauts.aggregate(total=Sum('spacewalks'))['total']
    # spacecraft = last_completed_mission.spacecraft.name
    #
    # return (f"The last completed mission is: {last_completed_mission.name}."
    #         f" Commander: {commander}. Astronauts: {', '.join(a.name for a in mission_astronauts)}."
    #         f" Spacecraft: {spacecraft}. Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    most_used_spacecraft = (Spacecraft.objects.annotate(missions_count=Count('used_in_mission', distinct=True))
                            .annotate(astronauts_count=Count('used_in_mission__astronauts', distinct=True))
                            .order_by('-missions_count', 'name')
                            .first())

    if not most_used_spacecraft or most_used_spacecraft.missions_count == 0:
        return 'No data.'

    return (f"The most used spacecraft is: {most_used_spacecraft.name},"
            f" manufactured by {most_used_spacecraft.manufacturer},"
            f" used in {most_used_spacecraft.missions_count} missions,"
            f" astronauts on missions: {most_used_spacecraft.astronauts_count}.")


def decrease_spacecrafts_weight():
    spacecrafts = (Spacecraft.objects
                   .filter(used_in_mission__status='Planned', weight__gte=200)
                   .distinct())

    if not spacecrafts:
        return 'No changes in weight.'

    num_of_spacecrafts_updated = spacecrafts.update(weight=F('weight') - 200)
    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {num_of_spacecrafts_updated} spacecrafts has been decreased."
            f" The new average weight of all spacecrafts is {avg_weight:.1f}kg")


