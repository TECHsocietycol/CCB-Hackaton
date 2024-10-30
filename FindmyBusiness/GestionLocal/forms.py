

from django import forms
from .models import PreferenciasUsuario


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Selecciona un archivo CSV')


class PreferenciasUsuarioForm(forms.ModelForm):
    class Meta:
        model = PreferenciasUsuario
        fields = ['precio_min', 'precio_max', 'area_min', 'area_max', 'localidad']    