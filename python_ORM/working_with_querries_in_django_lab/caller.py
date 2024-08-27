import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review


# Create and check models
def find_books_by_genre_and_language(book_genre: str, book_language: str) -> str:
    return Book.objects.filter(genre=book_genre, language=book_language)


def find_authors_nationalities() -> str:
    return '\n'.join(f"{a.first_name} {a.last_name} is {a.nationality}"
                     for a in Author.objects.exclude(nationality__isnull=True))


def order_books_by_year():
    return '\n'.join(f"{b.publication_year} year: {b.title} by {b.author}" for b in Book.objects
                     .all().order_by('publication_year', 'title'))


def delete_review_by_id(review_id: int) -> str:
    review_to_delete = Review.objects.get(id=review_id)
    review_to_delete.delete()
    return f'Review by {review_to_delete.reviewer_name} was deleted'


def filter_authors_by_nationalities(nationality: str) -> str:
    return '\n'.join(a.biography if a.biography else f"{a.first_name} {a.last_name}"
                     for a in Author.objects.filter(nationality=nationality).order_by('first_name', 'last_name'))


def filter_authors_by_birth_year(first_date: str, second_date: str) -> str:
    return '\n'.join(f"{a.birth_date}: {a.first_name} {a.last_name}"
                     for a in Author.objects.filter(birth_date__year__range=(first_date, second_date)).order_by('-birth_date'))


def change_reviewer_name(reviewer_name: str, new_name: str) -> QuerySet:
    Review.objects.filter(reviewer_name=reviewer_name).update(reviewer_name=new_name)
    return Review.objects.all()


# Run and print your queries
