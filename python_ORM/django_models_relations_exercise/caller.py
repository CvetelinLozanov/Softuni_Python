import datetime
import os
from datetime import timedelta, date, datetime

import django
from django.db.models import QuerySet, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Car, \
    Registration


def show_all_authors_with_their_books():
    result = []

    for a in Author.objects.all():
        books = a.book_set.all()

        if not books:
            continue

        books_string = ", ".join(b.title for b in books)
        result.append(f'{a.name} has written - {books_string}!')

    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.annotate(
        average_rating=Avg('reviews__rating')
    ).get(name=product_name)

    return product.average_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates() -> str:
    result = []

    for dl in DrivingLicense.objects.all().order_by('-license_number'):
        expiration_date = dl.issue_date + timedelta(days=365)
        result.append(f"License with number: {dl.license_number} expires on {expiration_date}!")

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    expiration_cutoff_date = due_date - timedelta(days=365)

    drivers_with_expired_licenses = Driver.objects.filter(
        license__issue_date__gt=expiration_cutoff_date,
    )

    return drivers_with_expired_licenses


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    registration.car = car
    registration.registration_date = date.today()

    car.save()
    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} with registration number"
            f" {registration.registration_number}.")


# Create queries within functions
