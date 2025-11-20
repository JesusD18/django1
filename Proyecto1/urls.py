from django.contrib import admin
from django.urls import path
from Proyecto1 import views  # 👈 Importamos las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('despedida/', views.despedida),

    # 👉 Página principal
    path('', views.home),
]
