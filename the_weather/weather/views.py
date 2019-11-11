import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.


def index(req):
    city = "Berlin"
    url = f"http://samples.openweathermap.org/data/2.5/weather?q={city}&appid=b6907d289e10d714a6e88b30761fae22"

    if req.method == 'POST':
        form = CityForm(req.POST)
        form.save()

    form = CityForm()

    r = requests.get(url).json()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'] - 273.15,
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(req, 'weather.html', context)
