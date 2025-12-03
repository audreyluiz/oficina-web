from django.urls import path

from clientes import views

urlpatterns = [
    path('lista', views.lista, name='lista'),
]