from django.urls import path
from . import views


urlpatterns = [
    path('', views.servise_home, name='servise_home'),
    path('usl/', views.usl, name='usl'),

]