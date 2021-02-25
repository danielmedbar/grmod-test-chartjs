from django.shortcuts import render
from django.http import HttpResponse

from .models import base_model

# Create your views here.
def bar_plots(request):
  labels = ['bcn','mad','val','sev']
  data = [200, 300, 150, 100]

  base_model_html = base_model.to_html()

  return render(request, 'plots.html', {
    'labels': labels,
    'data': data,
    'base_model': base_model_html,
  })
