# Generated by Django 5.0.3 on 2024-10-18 08:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Localidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("latitud_centro", models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    "longitud_centro",
                    models.DecimalField(decimal_places=6, max_digits=9),
                ),
                (
                    "radio_geografico",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Local",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("area_m2", models.DecimalField(decimal_places=2, max_digits=10)),
                ("descripcion", models.TextField()),
                ("direccion", models.CharField(max_length=255)),
                ("latitud", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitud", models.DecimalField(decimal_places=6, max_digits=9)),
                ("imagen_url", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "localidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="GestionLocal.localidad",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PreferenciasUsuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("precio_min", models.DecimalField(decimal_places=2, max_digits=10)),
                ("precio_max", models.DecimalField(decimal_places=2, max_digits=10)),
                ("area_min", models.DecimalField(decimal_places=2, max_digits=10)),
                ("area_max", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "localidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="GestionLocal.localidad",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
