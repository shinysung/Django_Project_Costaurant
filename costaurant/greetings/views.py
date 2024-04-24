from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloView(request):
    return HttpResponse("<h2>That's correct!</h2>")
