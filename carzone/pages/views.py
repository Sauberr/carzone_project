from django.shortcuts import render
from .models import Team


def home(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')