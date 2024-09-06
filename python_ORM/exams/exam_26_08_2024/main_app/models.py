from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

from main_app.managers import AuthorManager
from main_app.model_mixins import ContentFieldMixin, PublishedOnFieldMixin


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100),
        ]
    )

    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005)
        ]
    )

    website = models.URLField(
        null=True,
        blank=True,
    )

    objects = AuthorManager()

    def __str__(self):
        return self.full_name


class Article(ContentFieldMixin, PublishedOnFieldMixin, models.Model):

    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = "Technology", "Technology"
        SCIENCE = "Science", "Science"
        EDUCATION = "Education", "Education"

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(200),
        ]
    )

    category = models.CharField(
        max_length=10,
        default=CategoryChoices.TECHNOLOGY,
        choices=CategoryChoices,
        validators=[
            MaxLengthValidator(10)
        ],
    )

    authors = models.ManyToManyField(
        to=Author,
        related_name='articles'
    )

    def __str__(self):
        return self.title


class Review(ContentFieldMixin, PublishedOnFieldMixin, models.Model):
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return f"Review for {self.article.title} by {self.author.full_name}"


