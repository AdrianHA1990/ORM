from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import PersonalManage

# Create your models here.


class BaseDatos(models.Model):
    estado = models.BooleanField(default=True, verbose_name="Estado")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        abstract = True

class autor(BaseDatos):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

class Area(BaseDatos):
    nom_area = models.CharField(max_length=150, verbose_name="Area", null=False)

    def __str__(self):
        fila=str(self.id) + " " + self.nom_area
        return fila

class Estudio(BaseDatos):
    nom_est = models.CharField(max_length=150, verbose_name="Area", null=False, blank=False)

    def __str__(self):
        fila=self.nom_est
        return fila

carrera=(
    ('Sistemas', 'Sistemas'),
    ('Contabilidad', 'Contabilidad'),
    ('Derecho', 'Derecho'),
    ('Administracion', 'Administracion'),
    ('Diseño', 'Diseño'),
    ('Ingeniero', 'Ingeniero'),
    ('General', 'General'),

)

class personal(BaseDatos):
    name = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    ap = models.CharField(max_length=100, verbose_name="Apellido Paterno", null=False, blank=False)
    am = models.CharField(max_length=100, verbose_name="Apellido Materno", null=False, blank=False)
    foto = models.ImageField(upload_to='imagenes/', verbose_name="Foto", null=True, blank=True)
    area = models.ForeignKey(Area,verbose_name="Area",on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, verbose_name="Estudio", on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=100, verbose_name="Carrera", choices=carrera)

    objects = PersonalManage()

    def __str__(self):
        fila=str(self.id) + "_" + self.name + "_" + self.ap + "_" + self.am
        return fila
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
