from django.db import models
from django.db.models import Q

class PersonalManage(models.Manager):
    def todos(self):
        consulta= self.all().values("id","name","am","estado")[:10]
        return consulta
    def Mostrar_n(self, numero):
        consulta = self.all().values("id","name","am","estado")[:numero]
        return consulta
    def Buscar_nombre(self, nombre):
        consulta = self.filter(name=nombre).values("id","name","am","estado")
        return consulta
    def Buscar_nombre_p(self, palabra):
        consulta = self.filter(name__icontains=palabra).values("id","name","am","estado")
        return consulta
    def Buscar_nom_prin(self, palabra,n):
        consulta = self.filter(name__istartswith=palabra).values("id","name","am","estado").order_by("id")[:n]
        return consulta
    def Buscar_nom_ap(self, nombre, apellido, n):
        consulta = self.filter(Q(name__istartswith=nombre) | Q(ap__iendswith=apellido)
        ).values("id","name","ap","am","estado")[:n]
        return consulta
    def Buscar_nom_ap_am(self,palabra,n):
        consulta = self.filter(Q(name__istartswith=palabra) | Q(ap__iendswith=palabra) | Q(am__iendswith=palabra)
        ).values("id", "name", "ap", "am", "area" ,"estado")[:n]
        return consulta
    def Buscar_join(self,palabra,ar,n):
        consulta = self.filter(Q(name__icontains=palabra) | Q(ap__icontains=palabra)
        ).filter(Q(am__icontains=palabra) , Q(area=ar)
        ).values("id", "name", "ap", "am", "area")[:n]
        return consulta