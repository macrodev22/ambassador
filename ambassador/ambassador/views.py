from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    BASE_URL = request.build_absolute_uri('/')
    return HttpResponse(f"Hello there at {BASE_URL}")