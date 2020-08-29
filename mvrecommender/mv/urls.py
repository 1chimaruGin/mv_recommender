from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mood', views.mood, name='mood'),
    path('watch', views.watch, name='watch'),
]