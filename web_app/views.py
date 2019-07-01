from django.shortcuts import render

from django.shortcuts import render
import requests

def index(request):
    city_weather = requests.get('http://127.0.0.1:8000/api/weather/?city=london').json()

    weather = {
        'city': 'London',
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}
    return render(request, 'weather/index.html', context)