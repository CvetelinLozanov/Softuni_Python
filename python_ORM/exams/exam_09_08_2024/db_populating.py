import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# populate DB
from main_app.models import House, Dragon, Quest

# Sample Houses
house_stark = House.objects.create(
    name="Stark",
    motto="Winter is Coming",
    is_ruling=False,
    castle="Winterfell",
    wins=3
)

house_targaryen = House.objects.create(
    name="Targaryen",
    motto="Fire and Blood",
    is_ruling=True,
    castle="Dragonstone",
    wins=5
)

house_lannister = House.objects.create(
    name="Lannister",
    motto="Hear Me Roar",
    is_ruling=False,
    castle="Casterly Rock",
    wins=2
)

house_starks_enemy = House.objects.create(
    name="Enemy",
    motto="Starks are Down",
    is_ruling=False,
    wins=0
)

# Sample Dragons
dragon_drogon = Dragon.objects.create(
    name="Drogon",
    power=9.9,
    breath="Fire",
    is_healthy=True,
    birth_date='2020-5-17',
    wins=5,
    house=house_targaryen
)

dragon_rhaegal = Dragon.objects.create(
    name="Rhaegal",
    power=8.6,
    breath="Fire",
    is_healthy=True,
    birth_date='2020-5-17',
    wins=3,
    house=house_targaryen
)

dragon_viserion = Dragon.objects.create(
    name="Viserion",
    power=1.2,
    breath="Fire",
    is_healthy=False,
    birth_date='2020-5-17',
    wins=2,
    house=house_targaryen
)

dragon_syrax = Dragon.objects.create(
    name="Syrax",
    power=8.0,
    breath="Fire",
    is_healthy=True,
    birth_date='2021-5-17',
    wins=1,
    house=house_targaryen
)

dragon_silverwing = Dragon.objects.create(
    name="Silverwing",
    power=7.5,
    breath="Ice",
    is_healthy=True,
    birth_date='2021-6-17',
    wins=1,
    house=house_stark
)

dragon_shrykos = Dragon.objects.create(
    name="Shrykos",
    power=7.8,
    breath="Lightning",
    is_healthy=True,
    birth_date='2021-7-17',
    wins=2,
    house=house_stark
)

dragon_vermax = Dragon.objects.create(
    name="Vermax",
    power=7.8,
    breath="Fire",
    is_healthy=True,
    birth_date='2021-8-17',
    wins=1,
    house=house_lannister
)

# Sample Quests
quest1 = Quest.objects.create(
    name="Battle of Winterfell",
    code="BoW#",
    reward=500.0,
    start_time='2023-12-01 14:00:00+00:00',
    host=house_stark
)
quest1.dragons.set([dragon_shrykos, dragon_silverwing])

quest2 = Quest.objects.create(
    name="Siege of Meereen",
    code="SoM#",
    reward=1000.0,
    start_time='2024-06-24 15:00:00+00:00',
    host=house_targaryen
)
quest2.dragons.set([dragon_drogon, dragon_rhaegal, dragon_viserion])

quest3 = Quest.objects.create(
    name="Battle of Blackwater",
    code="BoB#",
    reward=700.0,
    start_time='2024-08-01 16:00:00+00:00',
    host=house_lannister
)
quest3.dragons.set([dragon_drogon, dragon_vermax])