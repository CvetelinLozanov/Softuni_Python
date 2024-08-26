import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from django.db.models import F


def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    result = []

    return '\n'.join(str(l) for l in Location.objects.all().order_by('-id'))


def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def add_cars():
    cars_info = ['Mercedes C63 AMG, 2019, white, 120000.00',
                     'Audi Q7 S line, 2023, black, 183900.00',
                     'Chevrolet Corvette, 2021, dark grey, 199999.00']
    cars = []

    for s in cars_info:
        model, year, color, price = s.split(', ')
        cars.append(Car(
            model=model,
            year=year,
            color=color,
            price=price,
        ))

    Car.objects.bulk_create(cars)


def apply_discount():
    all_cars = Car.objects.all()
    for c in all_cars:
        percentage = sum(int(ch) for ch in str(c.year)) / 100
        discount = float(c.price) * percentage
        c.price_with_discount = float(c.price) - discount

    Car.objects.bulk_update(all_cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    return '\n'.join(str(task) for task in Task.objects.filter(is_finished=False))


def complete_odd_tasks() -> None:
    Task.objects.annotate(odd=F('id') % 2).filter(odd=True).update(is_finished=True)


def encode_and_replace(text: str, task_title: str):
    Task.objects.filter(title=task_title).update(description=(''.join(chr(ord(ch) - 3) for ch in text)))


def get_deluxe_rooms() -> str:
    return '\n'.join(str(r) for r in HotelRoom.objects.annotate(odd=F('id') % 2).filter(room_type='Deluxe', odd=False))


def increase_room_capacity() -> None:
    all_rooms = HotelRoom.objects.all().order_by('id')
    prev_room_capacity = None

    for room in all_rooms:
        if not room.is_reserved:
            continue

        if prev_room_capacity is not None:
            room.capacity += prev_room_capacity
        else:
            room.capacity += room.id

        prev_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(all_rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    HotelRoom.objects.last().delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        points=F('points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        invertory='The inventory is empty'
    )

def fuse_characters(first_character: Character, second_character: Character):
    name = first_character.name + ' ' + second_character.name
    class_name = 'Fusion'
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ['Mage', 'Scout']:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()


# Create queries within functions
