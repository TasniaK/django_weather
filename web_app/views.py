from django.shortcuts import render
import requests
from .forms import CityForm

def index(request):
    if request.method == 'POST':
        # create a form instance and populate with data form thr request
        form = CityForm(request.POST)

        if form.is_valid():
            user_input = form.data
            city = user_input.get('city')
            city_weather = requests.get('http://127.0.0.1:8000/api/weather/?city={}'.format(city)).json()
            weather = {
                'city': city_weather['name'],
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            context = {'weather': weather, 'form': form}
            return render(request, 'weather/index.html', context)
        else:
            return render(request, 'weather/index.html', {'form': form})

        # if GET or any other method
    else:
        form = CityForm()
        return render(request, "weather/index.html", {'form': form})