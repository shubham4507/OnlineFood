from django.shortcuts import render
from django.http import HttpResponse

def home(resuqst):
    return render(resuqst, 'home.html')