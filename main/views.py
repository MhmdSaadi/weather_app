from django.shortcuts import render 
import json 
import urllib.request 
from django.conf import settings

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        api_key = settings.OPENWEATHER_API_KEY
        
        # source contain JSON data from API 
        source = urllib.request.urlopen( 
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        ).read() 

        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 

        # data for variable list_of_data 
        data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']), 
                "temp": str(round(kelvin_to_celsius(list_of_data['main']['temp']), 1)) + '°C', 
                "pressure": str(list_of_data['main']['pressure']) + ' hPa', 
                "humidity": str(list_of_data['main']['humidity']) + ' %', 
            }

        print(data) 
    else: 
        data ={} 
    return render(request, "main/index.html", data)
