from django.contrib import admin
from .models import *
# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'ap', 'am','area','estudio','Carrera','estado']
    search_fields = ['name', 'area']
    list_filter = ["area","estudio"]
    list_per_page = 10

admin.site.register(autor)
admin.site.register(personal,PersonalAdmin)
admin.site.register(Area)
admin.site.register(Estudio)

















