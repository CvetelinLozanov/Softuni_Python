from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from .validators import OnlyLettersValidator


# class OnlyLettersValidator:
#     def __init__(self, message='Fruit name should contain only letters!'):
#         self.message = message
#
#     def __call__(self, value):
#         if not value.isalpha():
#             raise ValidationError(self.message)
#
#     def deconstruct(self):
#         return (
#             'fruits.validators.OnlyLettersValidator',
#             (),
#             {'message': self.message}
#         )


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator()
        ]
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
    )
