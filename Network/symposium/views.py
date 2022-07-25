from django.shortcuts import render, redirect
from .models import Banner, Model_All, Point


Banners = Banner.objects.all()

# Landing page


def index(request):
    return render(request, 'symposium/index.html')

# Model view


def model(request, pk):
    Model_Display = Model_All.objects.get(slug=pk)
    Points = Point.objects.filter(model_link=Model_Display)
    return render(request, 'symposium/model.html', {"Model": Model_Display, "Points": Points})

# Exhibition booth


def exhibition(request):
    return render(request, 'symposium/exhibition_booth.html')

# Infodesk


def infodesk(request):
    return render(request, 'symposium/infodesk.html')

# Networking space


def networking(request):
    return render(request, 'symposium/networking.html')

# Lobby


def lobby(request):
    print(Banners)
    return render(request, 'symposium/lobby.html', {"Banners": Banners})
