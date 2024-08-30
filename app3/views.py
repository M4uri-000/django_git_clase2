from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html="""
        <h1>!HOLA¡</h1>
        <p>el rodrigo es el masca</p>
    """
    return HttpResponse(html)

def relleno(request):
    html="""
    <h1 style="color:purple">RENE PUENTE<h1/>
    <p>Con 2 zhipitia 2 tusi 2 rodrigos (perras) que saen malaya qlias</p>
    """
    return HttpResponse(html)
