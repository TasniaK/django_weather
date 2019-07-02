from django.http import JsonResponse

import requests

def weather_data(request):
    """Get raw data from public weather API"""
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8a34f3f503dfd53e88c467e4267b9cc9'
    city = request.GET.get('city', '')
    weather = requests.get(url.format(city)).json()

    return JsonResponse(weather)