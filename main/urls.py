from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('mark', views.mark, name='mark'),
    path('sail', views.sail, name='sail'),
    path('repair', views.repair, name='repair'),
    path('scladzp', views.scladzp, name='scladzp'),
    path('scladav', views.scladav, name='scladav'),
    path('model', views.model, name='model'),
    path('color', views.color, name='color'),
    path('about', views.about, name='about')

]