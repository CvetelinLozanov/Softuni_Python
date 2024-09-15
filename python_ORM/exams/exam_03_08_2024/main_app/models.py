from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models
from .validators import OnlyDigitsValidator
from .choices import StatusChoices
from .mixins import UpdatedAtMixin, NameMixin, LaunchDateMixin
from .managers import AstronautManager


# Create your models here.
class Astronaut(NameMixin, UpdatedAtMixin):

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{1,15}$')
        ]
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(NameMixin, UpdatedAtMixin, LaunchDateMixin):
    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )

    weight = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name


class Mission(NameMixin, LaunchDateMixin, UpdatedAtMixin):

    description = models.TextField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=9,
        choices=StatusChoices,
        default=StatusChoices.PLANNED,
    )

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
        related_name='used_in_mission',
    )

    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='missions',
    )

    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        related_name='mission_commander',
        null=True,
    )

    def __str__(self):
        return self.name
