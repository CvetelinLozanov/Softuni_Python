import os
from typing import Optional

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article
from django.db.models import Count, Avg, Max


# Create queries within functions
def get_authors(search_name=None, search_email=None) -> str:
    authors = ""
    if search_name is None and search_email is None:
        return ''

    elif search_name is not None and search_email is not None:
        authors = (Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email)
                   .order_by('-full_name'))

    elif search_name is not None and search_email is None:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')

    elif search_name is None and search_email is not None:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')

    result = []

    for a in authors:
        status = "Banned" if a.is_banned else "Not Banned"
        result.append(f"Author: {a.full_name}, email: {a.email}, status: {status}")

    return '\n'.join(result) if result else ''


def get_top_publisher() -> Optional[str | Author]:
    top_publisher = Author.objects.get_authors_by_article_count().first()
    if not top_publisher or top_publisher.articles_count == 0:
        return ''
    return f"Top Author: {top_publisher.full_name} with {top_publisher.articles_count} published articles."


def get_top_reviewer() -> str:
    top_reviewer = Author.objects.annotate(reviews_count=Count('reviews')).order_by('-reviews_count', 'email').first()
    if not top_reviewer or top_reviewer.reviews_count == 0:
        return ''
    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.reviews_count} published reviews."


def get_latest_article():
    last_article = (Article.objects.prefetch_related('authors', 'reviews').order_by('-published_on')
                    .annotate(avg_rating=Avg('reviews__rating')).first())

    if not last_article:
        return ''

    authors = ', '.join(a.full_name for a in last_article.authors.all().order_by('full_name'))
    reviews_count = last_article.reviews.count()
    avg_rating = last_article.avg_rating if last_article.avg_rating else 0.0

    return (f"The latest article is: {last_article.title}. Authors: {authors}."
            f" Reviewed: {reviews_count} times. Average Rating: {avg_rating:.2f}.")


def get_top_rated_article():
    top_rated_article = (Article.objects.prefetch_related('reviews')
                         .annotate(avg_rating=Avg('reviews__rating'))
                         .order_by('-avg_rating', 'title').first())

    reviews_count = top_rated_article.reviews.count() if top_rated_article else 0.0

    if top_rated_article is None or reviews_count == 0:
        return ''

    avg_rating = top_rated_article.avg_rating if top_rated_article.avg_rating else 0.0

    return (f"The top-rated article is: {top_rated_article.title},"
            f" with an average rating of {avg_rating:.2f}, reviewed {reviews_count} times.")


def ban_author(email=None):
    author = Author.objects.filter(email=email).first()

    if not author or email is None:
        return 'No authors banned.'

    author.is_banned = True
    author.save()
    reviews_count = author.reviews.count()

    author.reviews.all().delete()
    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."

