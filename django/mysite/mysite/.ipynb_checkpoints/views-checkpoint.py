from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello")

def index(request):
    context={
        "myname":"Neeraj",
    }
    return render(request,'views/index.html')