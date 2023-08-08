from django.shortcuts import render, HttpResponse
import urllib.request
import json

def hola(request):
    url = 'http://codealberti1997.pythonanywhere.com/api/productos/'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    return HttpResponse(data)