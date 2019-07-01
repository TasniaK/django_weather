from django.shortcuts import render
import requests
from .forms import CityForm, LoginForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        import pdb; pdb.set_trace()
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Invalid login details'
            return render(request, 'weather/login.html', {'error': error, 'form': form})
    else:
        form = LoginForm()
        return render(request, 'weather/login.html', {'form': form})


@login_required(login_url='/login')
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