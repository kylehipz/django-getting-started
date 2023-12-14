from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    text = bytes("Hello, world!!!! This is from kyle", "utf-8")
    return HttpResponse(text)
