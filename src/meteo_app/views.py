from django.shortcuts import render, loader
import geocoder, requests
from django.http import HttpResponse, HttpRequest
from .models import Cities


def get_form(request):
    return render(request, template_name="index.html")


def get_temp_here(request: HttpRequest):
    coordinates = geocoder.ip('me').latlng
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&current=temperature_2m&timezone=Europe%2FMoscow&forecast_days=1"
    result = requests.get(api_url).json()

    current_temp = result["current"]["temperature_2m"]

    context = {"location": "Температура в вашем месте:",
               "temp": str(current_temp) + "℃"}

    return render(request, template_name="index.html", context=context)


def get_temp_in_other_city(request: HttpRequest):
    if request.method == 'POST':
        if 'other' in request.POST:
            country_input = request.POST['country']
            city_input = request.POST['city']

            city = Cities.objects.get(country=str(country_input), city_ascii=str(city_input))
            city_lat = city.lat
            city_lgt = city.lng
            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lgt}&current=temperature_2m&timezone=Europe%2FMoscow&forecast_days=1"
            result = requests.get(api_url).json()

            current_temp = result["current"]["temperature_2m"]

            context = {"location": f"Температура в городе {city_input}:",
                       "temp": str(current_temp) + "℃"}

            return render(request, template_name="index.html", context=context)

        elif 'here' in request.POST:
            coordinates = geocoder.ip('me').latlng
            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&current=temperature_2m&timezone=Europe%2FMoscow&forecast_days=1"
            result = requests.get(api_url).json()

            current_temp = result["current"]["temperature_2m"]

            context = {"location": "Температура в вашем месте:",
                       "temp": str(current_temp) + "℃"}

            return render(request, template_name="index.html", context=context)

    else:
        return render(request, template_name="index.html")
