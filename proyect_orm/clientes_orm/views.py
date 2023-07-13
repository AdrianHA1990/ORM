
# Create your views here.
from django.shortcuts import render
# from django.views.generic import TemplateView,CreateView,Update,DeleteView,ListView
from .models import *


def lista(request):
    consulta = personal.objects.filter(name__iregex='(^Ar[e]?)').order_by('name')
    #consulta = personal.objects.filter(fecha_registro__year='2021').order_by('name')
    #consulta = personal.objects.filter(fecha_registro__range=("2022-04-01", "2022-06-01")).order_by('name')
    #consulta = personal.objects.filter(fecha_registro__gte="2022-12-01").order_by('name')
    #consulta = personal.objects.filter(am__endswith="th").order_by('name')
    #consulta = personal.objects.filter(name__istartswith="ab").order_by('name')
    #consulta = personal.objects.filter(name__startswith="Cl").order_by('name')
    #consulta = personal.objects.filter(id__lte=10).order_by('name')
    # consulta = personal.objects.filter(id__gte=970).order_by("name")

    # consulta = personal.objects.all()
    # consulta = personal.objects.all()[:50]
    # consulta = personal.objects.all().order_by('name','Carrera')[:20]
    #consulta = personal.objects.filter(ap__icontains="Ab")
    #consulta = personal.objects.filter(id__in=[2,522,755]).values()
    #consulta = personal.objects.filter(name__icontains="or").values("id","name","Carrera","estudio","estado")
    # consulta = personal.objects.filter(id__gt=100).order_by('name')[:20]
    # consulta = personal.objects.filter(id__lt=50).order_by('name')[:50]


    return render(request, 'crud/lista.html',{"consulta":consulta})


