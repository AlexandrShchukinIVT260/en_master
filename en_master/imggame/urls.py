from django.urls import path
from . import views

urlpatterns = [
    path('', views.img_game, name='img_game')
]