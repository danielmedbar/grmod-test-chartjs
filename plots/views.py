from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_plot(request):
  return HttpResponse("Hello, world. This is the site for plots.")

def bar_plots(request):
  labels = ['bcn','mad','val','sev']
  data = [200, 300, 150, 100]

  return render(request, 'plots.html', {
    'labels': labels,
    'data': data,
  })

