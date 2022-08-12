from django.contrib import admin
from .models import Cliente, Tarjeta, ClienteTarjeta, Revista, Personaje,ArticuloColeccionable

#class ClienteAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
#    list_display = ("id", "user", "fechaNacimiento", "genero", "tipo")


#class TarjetaAdmin(admin.ModelAdmin):
#    # Se sobre escribe lo que hace __str__
#    list_display = ("nombre", "descripcion", "interes")


#class ClienteTarjetaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
#    list_display = ("numeroTarjeta", "cliente", "tarjeta", "creditoMax")

#class ClienteAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
#    list_display = ("id", "user", "fechaNacimiento", "genero", "tipo")


#class RevistaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
#    list_display = ("nombre", "id","descripcion", "compania","anio")    


#class PersonajeAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
#    list_display = ("nombre", "id","descripcion", "genero","tipo","compania")


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tarjeta)
admin.site.register(ClienteTarjeta)
admin.site.register(Revista)
admin.site.register(Personaje)
admin.site.register(ArticuloColeccionable)

