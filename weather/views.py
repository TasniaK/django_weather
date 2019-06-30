from django.http import JsonResponse

import requests

def weather_data(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8a34f3f503dfd53e88c467e4267b9cc9'
    weather = requests.get(url).json()

    return JsonResponse(weather)