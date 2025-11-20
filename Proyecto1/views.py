from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Mi primer página con Django Jesus Alejandro Diaz Serafin")

def despedida(request):
    return HttpResponse("Seguiremos aprendiendo Django ")
