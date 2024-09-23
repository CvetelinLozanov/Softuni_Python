from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from main_app.managers import HouseManager
from main_app.mixins import NameMixin, ModifiedMixin, WinMixin


# Create your models here.
class House(NameMixin, ModifiedMixin, WinMixin):
    motto = models.TextField(
        null=True,
        blank=True,
    )

    is_ruling = models.BooleanField(
        default=False,
    )

    castle = models.CharField(
        max_length=80,
        null=True,
        blank=True,
    )

    objects = HouseManager()

    def __str__(self):
        return self.name


class Dragon(NameMixin, ModifiedMixin, WinMixin):
    class BreathChoices(models.TextChoices):
        FIRE = 'Fire', 'Fire'
        ICE = 'Ice', 'Ice'
        LIGHTNING = 'Lightning', 'Lightning'
        UNKNOWN = 'Unknown', 'Unknown'

    power = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        default=1,
    )

    breath = models.CharField(
        max_length=9,
        choices=BreathChoices,
        default=BreathChoices.UNKNOWN,
    )

    is_healthy = models.BooleanField(
        default=True,
    )

    birth_date = models.DateField(
        default=date.today
    )

    house = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='dragons'
    )

    def __str__(self):
        return self.name


class Quest(NameMixin, ModifiedMixin):
    code = models.CharField(
        max_length=4,
        validators=[
            RegexValidator(r'^[a-zA-Z#]{4}$')
        ],
        unique=True,
    )

    reward = models.FloatField(
        default=100,
    )

    start_time = models.DateTimeField()

    dragons = models.ManyToManyField(
        to=Dragon,
        related_name='quests'
    )

    host = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
        related_name='quests',
    )

    def __str__(self):
        return self.name
