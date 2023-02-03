from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador
# MVT = Modelo Vista Template


def hola_mundo(request):
    return HttpResponse("ESA GENTE")
