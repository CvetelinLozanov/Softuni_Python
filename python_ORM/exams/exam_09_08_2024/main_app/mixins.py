from django.core.validators import MinLengthValidator
from django.db import models


class NameMixin(models.Model):
    name = models.CharField(
        max_length=80,
        validators=[
            MinLengthValidator(5)
        ],
        unique=True,
    )

    class Meta:
        abstract = True


class ModifiedMixin(models.Model):
    modified_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class WinMixin(models.Model):
    wins = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        abstract = True
