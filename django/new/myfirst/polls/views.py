# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def details(request,question_id):
     response = "You're looking at the results of question %s."
     return HttpResponse(response % question_id)

def results(request,id):
     response = "Your id is %s"
     return HttpResponse(response % id)

def index(request):
     template = loader.get_template('index.html')
     context={
          "my":"Hello how are you"
     }
     return HttpResponse(template.render(context, request))

# Create your views here.
