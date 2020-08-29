import pandas as pd 
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'mv/landing.html')

def mood(request):
    return render(request, 'mv/movielist.html')

def watch(request):
    return render(request, 'mv/watch.html')
