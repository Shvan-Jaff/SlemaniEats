
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'home.html', {'now': datetime.now()})

def map_view(request):
    return render(request, 'map.html', {'now': datetime.now()})

def categories(request):
    return render(request, 'categories.html', {'now': datetime.now()})
