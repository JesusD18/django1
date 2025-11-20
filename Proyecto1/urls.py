from django.contrib import admin
from django.urls import path
from Proyecto1 import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo),
    path('despedida/', views.despedida),
]
