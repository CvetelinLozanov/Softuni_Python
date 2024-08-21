from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('test/', views.test_func),
    path('all-users/', views.show_all_users),
]
