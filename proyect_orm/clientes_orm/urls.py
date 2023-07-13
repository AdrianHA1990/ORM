from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = "clientes_orm_app"

urlpatterns =[
    path('lista', views.lista, name='lista'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
