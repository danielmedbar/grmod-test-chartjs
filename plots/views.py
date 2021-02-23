from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_plot(request):
  return HttpResponse("Hello, world. This is the site for plots.")

