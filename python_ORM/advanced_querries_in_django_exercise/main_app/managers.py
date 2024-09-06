from decimal import Decimal

from django.db import models
from django.db.models import Count, QuerySet, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self) -> QuerySet:
        return self.values('location').annotate(location_count=Count('id')).order_by('-location_count','location')[:2]


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.all().order_by('-rating').first()

    def lowest_rated_game(self):
        return self.all().order_by('rating').first()

    def average_rating(self):
        average_rating = self.aggregate(Avg('rating'))
        return round(average_rating['rating__avg'], 1)