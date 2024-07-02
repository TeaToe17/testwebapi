from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests

@csrf_exempt
@require_http_methods(["GET"])
def index(request):
    name_param = request.GET.get('name')
    response = requests.get("http://ip-api.com/json/")
    print(response)
    # response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Nigeria,uk&appid=`f7f3fa42b9dae1fdc57fe1fc800a93f2`")
    ip_address,country = response.json().get("query"),response.json().get("country")
    if name_param:
        message = {
            "client_ip":ip_address,
            "location":country,
            "greetings":f'Hello, {name_param}!'
            }
    return JsonResponse (message,safe=False)
