from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def index(request):
    return render(request, 'index.html', {'error': 'loi'})
