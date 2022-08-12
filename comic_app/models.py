from django.db import models

# Create your models here.


from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    """ Define la tabla Perfil """
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    TIPO = [
        ("PF", "Persona Física"),
        ("PM", "Persona Moral"),
    ]
    tipo = models.CharField(max_length=45, choices=TIPO, null=True, blank=True)

class Personaje(models.Model):
    """ Define la tabla Perfil """
    nombre = models.CharField(max_length=200, null=False, blank=False)
    id=models.AutoField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )
    descripcion=models.TextField(blank=False)
    GENERO = [
        ("M", "Mutante"),
        ("H", "Humano"),
        ("E", "Extraterrestre"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    TIPO = [
        ("Heroe", "Héroe"),
        ("Villano", "Villano"),
    ]
    tipo = models.CharField(max_length=45, choices=TIPO, null=True, blank=True)
    COMPANIA = [
        ("Marvel", "Marvel"),
        ("DC", "DC Comics"),
        ("Dark Horse", "Dark Horse"),
        ("IDW", "IDW Publishing"),
    ]
    compania= models.CharField(max_length=45, choices=COMPANIA, null=True, blank=True)
    

class Revista(models.Model):
    """ Define la tabla Perfil """
    nombre = models.CharField(max_length=200, null=False, blank=False)
    id=models.AutoField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )
    descripcion=models.TextField(blank=False)
    
    COMPANIA = [
        ("Marvel", "Marvel"),
        ("DC", "DC Comics"),
        ("Dark Horse", "Dark Horse"),
        ("IDW", "IDW Publishing"),
    ]
    compania= models.CharField(max_length=45, choices=COMPANIA, null=True, blank=True)
    anio=models.IntegerField(null=False, blank=False)

class Tarjeta(models.Model):
    """ Define la tabla Tarjeta """
    nombre = models.CharField(max_length=145)
    descripcion = models.CharField(max_length=256)
    interes = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre


class ClienteTarjeta(models.Model):
    """ Define la tabla Cliente Tarjeta """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    numeroTarjeta = models.IntegerField()
    creditoMax = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.numeroTarjeta)

class ArticuloColeccionable(models.Model):
    """ Define la tabla Perfil """
    nombre = models.CharField(max_length=200, null=False, blank=False)
    id=models.AutoField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID'
                )
    descripcion=models.TextField(blank=False)
    
    COMPANIA = [
        ("Marvel", "Marvel"),
        ("DC", "DC Comics"),
        ("Dark Horse", "Dark Horse"),
        ("IDW", "IDW Publishing"),
    ]
    compania= models.CharField(max_length=45, choices=COMPANIA, null=True, blank=True)
    anio=models.IntegerField(null=False, blank=False)
    nuevo=models.IntegerField(null=False, blank=False)
    
    ESTADO = [
        ("Excelente", "Excelente"),        
        ("Bueno", "Bueno"),
        ("Regular", "Regular"),
        ("Malo", "Malo"),
    ]  
    estado= models.CharField(max_length=45, choices=ESTADO, null=True, blank=True)
    




        