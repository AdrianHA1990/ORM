from django.db import models
from django.db.models import Q

class PersonasManager(models.Manager):
    def Todas(self):
        consulta = self.all().values("id","name","estado")
        return consulta
    def Buscar_nom(self,nombre,n ):
        consulta = self.filter(name__icontains=(nombre)).order_by("id").values("id","name","estado","interes")[:n]
        return consulta

    def Buscar_nom_interes(self, nombre, n):
        consulta = self.filter(name__icontains=(nombre)).values("id", "name", "estado", "interes")[:n]
        return consulta