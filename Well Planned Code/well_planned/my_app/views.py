from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import TodoListCatagory
from .models import DairyCatagory
from expensetrack.models import Income
from django.http import HttpResponseRedirect
import requests

def Home(request):

    Todo_List = TodoListCatagory.objects.all()
    Dairy_list = DairyCatagory.objects.all()
    income = Income.objects.get(id = 1)
    context = {
        'Todo_list': Todo_List,
        'Dairy_list': Dairy_list,
        'income': income,
    }
    return render(request, 'my_app/Home.html/', context)


def Weather(request):

    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "Bangalore"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        '''print(" Temperature in kelvin unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                str(weather_description))'''
        context = {
            "temperature": str(current_temperature),
            "humidity": str(current_humidiy),
            "description": str(weather_description),
        }

    else:
        print(" City Not Found ")

    return render(request, 'my_app/weather.html/',context)
