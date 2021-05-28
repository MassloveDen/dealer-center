from django.shortcuts import render
from .models import D_c
# Create your views here.

def servise_home(request):
    servise = D_c.objects.all()
    return render(request, 'servise/servise_home.html', {'servise':servise})

def usl(request):
    return render(request, 'servise')

