from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Local
import pandas as pd
import csv
from django.db import transaction
from django.utils.datastructures import MultiValueDictKeyError
import folium


def actualizar_inventario(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']  # Obtenemos el archivo cargado
        except MultiValueDictKeyError:
            messages.error(request, "Error: No se ha cargado ningún archivo.")
            return redirect('actualizar_inventario')

        # Verificamos que el archivo sea un CSV
        if not file.name.endswith('.csv'):
            messages.error(request, "El archivo no es un CSV válido.")
            return redirect('actualizar_inventario')

        try:
            # Leemos el archivo CSV con pandas
            df = pd.read_csv(file)
        except Exception as e:
            messages.error(request, f"Error al procesar el archivo: {e}")
            return redirect('actualizar_inventario')

        # Transacción para asegurar que la carga se realiza correctamente
        with transaction.atomic():
            for _, row in df.iterrows():
                Local.objects.update_or_create(
                    titulo=row['Titulo'],
                    defaults={
                        'precio': row['Precio'],
                        'area': row['Area'],
                        'localidad': row['Localidad'],
                        'descripcion': row['Descripcion']
                    }
                )

        messages.success(request, "El inventario ha sido actualizado correctamente.")
        return redirect('consultar_locales')

    return render(request, 'actualizar_inventario.html')


def consultar_locales(request):
    precio_min = request.GET.get('precio_min', 0)
    precio_max = request.GET.get('precio_max', 999999999)
    area_min = request.GET.get('area_min', 0)
    area_max = request.GET.get('area_max', 999999)
    localidad = request.GET.get('localidad', '')

    locales = Local.objects.filter(
        precio__gte=precio_min,
        precio__lte=precio_max,
        area__gte=area_min,
        area__lte=area_max
    )

    if localidad:
        locales = locales.filter(localidad__icontains=localidad)

    return render(request, 'consultar_locales.html', {'locales': locales})


def cargar_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        if not file.name.endswith('.csv'):
            messages.error(request, "Error: No se ha cargado un archivo CSV válido.")
            return redirect('cargar_csv')

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        with transaction.atomic():
            for row in reader:
                Local.objects.update_or_create(
                    titulo=row['Titulo'],
                    defaults={
                        'precio': row['Precio'],
                        'area': row['Area'],
                        'localidad': row['Localidad'],
                        'descripcion': row['Descripcion'],
                    }
                )

        messages.success(request, "Datos cargados correctamente.")
        return redirect('consultar_locales')
    else:
        return render(request, 'cargar_csv.html')


def mostrar_mapa_locales(request):
    mapa = folium.Map(location=[4.7110, -74.0721], zoom_start=12)

    locales = Local.objects.all()

    for local in locales:
        if local.latitud and local.longitud:
            folium.Marker(
                location=[local.latitud, local.longitud],
                popup=f"{local.titulo} - {local.localidad}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(mapa)

    mapa_html = mapa._repr_html_()
    return render(request, 'mapa_locales.html', {'mapa': mapa_html})


def eliminar_local(request, local_id):
    local = Local.objects.get(id=local_id)
    local.delete()
    messages.success(request, "El local ha sido eliminado.")
    return redirect('consultar_locales')


def eliminar_todo_inventario(request):
    Local.objects.all().delete()
    messages.success(request, "Todo el inventario ha sido eliminado.")
    return redirect('consultar_locales')


def editar_local(request, local_id):
    local = Local.objects.get(id=local_id)

    if request.method == "POST":
        local.titulo = request.POST['titulo']
        local.precio = request.POST['precio']
        local.area = request.POST['area']
        local.localidad = request.POST['localidad']
        local.descripcion = request.POST['descripcion']
        local.save()
        messages.success(request, "El local ha sido actualizado.")
        return redirect('consultar_locales')

    return render(request, 'editar_local.html', {'local': local})


def inicio_inmuebles(request):
    return render(request, 'inicio_inmuebles.html')


