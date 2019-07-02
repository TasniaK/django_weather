from django.shortcuts import render
import requests
from .forms import CityForm, LoginForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    """Prompt user to login when hitting homepage."""

    # if user tries to log in.
    if request.method == 'POST':

        # for instance with login details from request.
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # success.
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        # redirect to login page but show error.
        else:
            error = 'Invalid login details'
            return render(request, 'weather/login.html', {'error': error, 'form': form})

    # for any requests other than POST.
    else:
        form = LoginForm()
        return render(request, 'weather/login.html', {'form': form})


@login_required(login_url='/login')
def index(request):
    """Get data from weather app endpoint, filter and show on homepage (UI)."""

    if request.method == 'POST':
        # form instance with data from the request (the city).
        form = CityForm(request.POST)

        # form validation.
        if form.is_valid():
            # grab city from user input.
            user_input = form.data
            city = user_input.get('city')
            # populate weather app API endpoint with city name
            city_weather = requests.get('http://127.0.0.1:8000/api/weather/?city={}'.format(city)).json()

            # filter data from endpoint.
            weather = {
                'city': city_weather['name'],
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            context = {'weather': weather, 'form': form}

            # return a page, and send filtered weather data to index.html
            return render(request, 'weather/index.html', context)

        else:
            return render(request, 'weather/index.html', {'form': form})

        # if GET or any other method.
    else:
        form = CityForm()
        return render(request, "weather/index.html", {'form': form})