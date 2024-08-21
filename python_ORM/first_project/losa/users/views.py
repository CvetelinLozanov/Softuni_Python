from django.shortcuts import render
from django.http import HttpResponse, response
from .models import User

# Create your views here.


def test_func(request):
    return HttpResponse("Hello There")


def show_all_users(request):
    #all = User.objects.all()
    all = User.objects.filter(name__startswith="A")
    payload = {'users': all}
    return render(request, 'users/all-users.html', context=payload)