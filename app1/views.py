from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>soy el index de la app1</h1>")

def presentacion(request):
    html="""
        <p>soy un parrafo de app1</p>
        <h2>soy un subtitulo de app1</h2>
    """
    return HttpResponse(html)