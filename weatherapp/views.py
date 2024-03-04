from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        res =  urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'6a0a8e5b129c6238ebf3195d7927099f').read()
        json_data = json.loads(res) 
        data = {
            "country_code": str(json_data['sys']['country']),
            "temperature": float(json_data['main']['temp'])+'k',
            "description": json_data['weather'][0]['description'],
            "coordinates": str(json_data['coord']['lon'])+ '' + str(json_data['cord']['lat']),
            "pressure": str(json_data['main']['pressure']),
            'humidty': str(json_data['main']['humidity']),
            
            }
    else:
        data = {}
    return render(request, 'index.html', data )