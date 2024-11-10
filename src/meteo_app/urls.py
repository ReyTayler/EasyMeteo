from django.urls import path
from .views import get_temp_in_other_city, get_form

urlpatterns = [
    path('meteo/', get_temp_in_other_city),
    #path('meteo/here', get_temp_here),
]
