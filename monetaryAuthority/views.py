from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html=("<html>"
    "<head></head>"
    "<body>this is ma.views.index</body>"
    "</html>")
    return HttpResponse(html)

