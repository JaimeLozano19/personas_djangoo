from django.http import HttpResponse
from django.shortcuts import render

from registro.models import Persona


# Create your views here.
def bienvenido(request):
    no_personas_var = Persona.objects.count()
    #registro = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas':no_personas_var, 'registro': personas})



