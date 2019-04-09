from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    faculties=Faculties.objects.all()
    args = {'faculties': faculties, }
    return render(request, 'index.html', args)