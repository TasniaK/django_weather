from django.urls import path

from . import views

urlpatterns = [
    path('weather/', views.weather_data, name='weather_data'),

]