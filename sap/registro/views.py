import requests
from django.shortcuts import render
from .forms import FormularioRegistro

def registro(request):
    ciudad_options = None
    ciudad_selected = None

    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            # Call the API to obtain the list of cities
            response = requests.get('https://www.datos.gov.co/resource/xdk5-pm3f.json')

            if response.status_code == 200:
                datos_api = response.json()
                # Assuming the API returns a list of cities, extract municipality names
                ciudad_options = [city['municipio'] for city in datos_api] if datos_api else None
                # Assuming you want to set the selected city to the first one
                ciudad_selected = ciudad_options[0] if ciudad_options else None

            form.save()

            # Create a new instance of the form to clear the data
            form = FormularioRegistro()
    else:
        form = FormularioRegistro()

    return render(request, 'registro/registro.html', {'form': form, 'ciudad_options': ciudad_options, 'ciudad_selected': ciudad_selected})
