from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import PersonasManager

# Create your models ere.

class BaseDatos(models.Model):
    estado = models.BooleanField(default=True, verbose_name="Estado")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha Registro")
    fecha_modificacion = models.DateField(auto_now_add=True, verbose_name="Fecha Modificacion")

    class Meta:
        abstract = True


class Interes(BaseDatos):
    nombre_interes = models.CharField(max_length=50,verbose_name="Interes")

    def __str__(self):
        dato = str(self.id) + "  " + self.nombre_interes + "  " + str(self.estado)
        return dato

class Personas(BaseDatos):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    interes = models.ManyToManyField(Interes, related_name="interes")

    def __str__(self):
        dato = str(self.id) + "  " + self.name
        return dato

    objects = PersonasManager()

class DatosP(BaseDatos):
    persona = models.OneToOneField(Personas, on_delete=models.CASCADE)
    pais = models.CharField(max_length=50, verbose_name="Pais")
    nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")
    direction = models.CharField(max_length=50, verbose_name="Direccion")
    tel = models.CharField(max_length=50, verbose_name="Telefono")
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(verbose_name="Email",max_length=70)

    def __str__(self):
        dato = str(self.id) + "  " + str(self.persona) + "  " + self.pais + " " + self.nacionalidad
        return dato

# Ficha de auto

class FichaAuto(BaseDatos):
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    color = models.CharField(max_length=50, verbose_name="Color")
    year = models.CharField(max_length=50, verbose_name="Año")
    costo = models.FloatField(verbose_name="Costo", default=0)
    dias_renta = models.PositiveBigIntegerField(default=0, verbose_name="Dias")


    def __str__(self):
        dato = str(self.id) + "  " + self.modelo + "  " + self.marca
        return dato

class Categorias(BaseDatos):
    name_categorias = models.CharField(max_length=50, verbose_name="Categorias")

    def __str__(self):
        dato = str(self.id) + "  " + self.name_categorias
        return dato


class Auto(BaseDatos):
    ficha = models.ForeignKey(FichaAuto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        dato = str(self.id) + "  " + str(self.ficha) + "  " + str(self.categoria)
        return dato

class Prestamo(BaseDatos):
    person = models.OneToOneField(Personas, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fecha_dev = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        dato = str(self.id) + "  " + str(self.person) + "  " + str(self.auto)
        return dato