"""
URL configuration for InventarioITS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from GestionLocal import views

urlpatterns = [
    path('', views.inicio_inmuebles, name='inicio_inmuebles'),  # Ruta para inicio_inmuebles
    path('consultar_locales/', views.consultar_locales, name='consultar_locales'),    # Vista principal para consultar locales # Vista para cargar locales
    path('map/', views.mostrar_mapa_locales, name='mostrar_mapa_locales'),
    path('actualizar_inventario/', views.actualizar_inventario, name='actualizar_inventario'),
    path('map/', views.mostrar_mapa_locales, name='mostrar_mapa_locales'), #ta para mostrar el mapa # Vista para agregar preferencias del usuario
]
