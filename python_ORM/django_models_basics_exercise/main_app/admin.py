from django.contrib import admin
from django.contrib.admin import ModelAdmin

from main_app.models import Book


admin.site.register(Book)
