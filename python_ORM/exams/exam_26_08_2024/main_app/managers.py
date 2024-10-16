from django.db import models
from django.db.models import Count, QuerySet


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self) -> QuerySet:
        return self.annotate(articles_count=Count('articles')).order_by('-articles_count', 'email')
