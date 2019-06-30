from django.shortcuts import render

from django.shortcuts import render

def index(request):
    weather = {
        'city': 'Las Vegas',
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}
    return render(request, 'weather/index.html', context)