from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a mi proyecto Django en Vercel</h1><p>Todo funciona correctamente 🎉</p>")
