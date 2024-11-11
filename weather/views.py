from django.shortcuts import render
import json
import urllib.request

def index(request):
    data = {}  # Initialize data as an empty dictionary
    city_name = ""  # Initialize an empty string for the city name
    if request.method == 'POST':
        city_name = request.POST['city']  # Get the city name from the form
        try:
            # Fetch data from the OpenWeatherMap API
            res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=036c00f59d6b5ffa854363e481b81f44').read()
            json_data = json.loads(res)
            data = {
                "city": city_name,  # Pass the city name to the template
                "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
                "temp": f"{json_data['main']['temp']}K",  # Temperature in Kelvin
                "pressure": f"{json_data['main']['pressure']} hPa",  # Pressure in hectopascals
                "humidity": f"{json_data['main']['humidity']}%",  # Humidity in percentage
                "description": json_data['weather'][0]['description'],  # Weather description
            }
        except Exception as e:
            data = {"error": "City not found or error with API. Please try again."}

    return render(request, 'index.html', data)
