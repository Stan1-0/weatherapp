from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        res =  urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=6a0a8e5b129c6238ebf3195d7927099f').read()
        json_data = json.loads(res) 
        data = {
            "Country_code": str(json_data['sys']['country']),
            "Temperature": str(float(json_data['main']['temp']))+'k',
            "Description": json_data['weather'][0]['description'],
            "Coordinates": str(json_data['coord']['lon'])+ '' + str(json_data['coord']['lat']),
            "Pressure": str(json_data['main']['pressure'])+'hpa',
            "Humidity": str(json_data['main']['humidity'])+'%',
            
            
            }
    else:
        data = {}
    return render(request, 'index.html', data )