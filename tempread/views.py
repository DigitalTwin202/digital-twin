from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    #response = requests.get('http://api.open-notify.org/astros.json')
    #print(response.json())
    data = {
        'data': {
            'lat': 11.0168,
            'long': 76.9558,
        }


    }

    return render(request,template_name='tempread/hello.html', context=data)