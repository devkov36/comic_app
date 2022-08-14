from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#sfrom .models import Tarjeta, ClienteTarjeta
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarjeta, Revista

def index(request):
   """ Vista para atender la petición de la url GET / """
   return render(request, "comic_app/index.html")

def acerca_de(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    return render(request, "comic_app/acerca-de.html")

def login(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    return render(request, "comic_app/login.html")
def registro(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    return render(request, "comic_app/registro.html")
def comic(request):
    """ Vista o función que atiende la url GET /acerca-de/ """
    revistas_all = Revista.objects.all()
    return render(request, "comic_app/comic.html",
        {
            "revistas": revistas_all,
        }
    )
    