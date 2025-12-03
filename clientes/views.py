from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from clientes.models import Cliente


# Create your views here.
def lista(request):
    clientes = Cliente.objects.all()

    context = {
        "clientes": clientes,
    }
    template = loader.get_template("clientes.html")
    return HttpResponse(template.render(context, request))
