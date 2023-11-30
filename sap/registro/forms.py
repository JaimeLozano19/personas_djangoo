from django import forms
from .models import Registrado
from django_select2.forms import Select2Widget
import requests



class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ['nombre', 'apellido', 'direccion', 'fecha_nacimiento', 'ciudad']
        ciudad = forms.ChoiceField(label='Ciudad', widget=Select2Widget)

        def __init__(self, *args, **kwargs):
            super( FormularioRegistro, self).__init__(*args, **kwargs)

            # Llamada a la API
            api_url = 'https://www.datos.gov.co/resource/xdk5-pm3f.json'
            response = requests.get(api_url)

            # Verifica si la solicitud fue exitosa
            if response.status_code == 200:
                data = response.json()

                # Extrae las opciones de la ciudad de la respuesta de la API
                ciudades = [(ciudad['nombre_municipio'], ciudad['nombre_municipio']) for ciudad in data]

                # Agrega las opciones al campo 'ciudad' en el formulario
                self.fields['ciudad'].choices = [('', 'Selecciona una ciudad')] + ciudades
            else:
                # Si la solicitud a la API falla, muestra un error en la consola
                print('Error al obtener datos de la API')
