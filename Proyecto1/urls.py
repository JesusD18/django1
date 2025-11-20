from django.contrib import admin
from django.urls import path
from Proyecto1 import views  # si tus vistas están ahí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('despedida/', views.despedida),

    # 👉 Nueva ruta para la página principal
    path('', views.saludo),  # o cualquier vista
]
