from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {
        'title': 'Дилеры',
        'values': ['Марка', 'Модель', 'Цвет'],
        'obj': {
            'mark': 'BMW',
            'model': 'x6',
            'color': 'black',
        }
    }
    return render(request, 'DC/home.html', data)

def about(request):
    return render(request, 'DC/about.html', data)

def mark(request):
    return render(request, 'DC/mark.html', data)

def sail(request):
    return render(request, 'DC/sail.html', data)

def repair(request):
    return render(request, 'DC/repair.html', data)

def scladzp(request):
    return render(request, 'DC/scladzp.html', data)

def scladav(request):
    return render(request, 'DC/scladav.html', data)

def model(request):
    return render(request, 'DC/model.html', data)

def color(request):
    return render(request, 'DC/color.html', data)



# Продажа, ремонт, склад з.п., склад авто.
# VIN: марка, модель, цвет.