from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#sfrom .models import Tarjeta, ClienteTarjeta
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   """ Vista para atender la petición de la url GET / """
   return render(request, "comic_app/index.html")

def acerca_de(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    return render(request, "comic_app/acerca-de.html")
