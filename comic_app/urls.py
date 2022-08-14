from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de/', views.acerca_de, name="acerca_de"),    
    path('login/', views.login, name="login"),
    path('comic/', views.comic, name="comic"),
    path('registro/', views.registro, name="registro"),    
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
