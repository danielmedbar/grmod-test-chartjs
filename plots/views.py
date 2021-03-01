from django.shortcuts import render
from django.http import HttpResponse

from .models import base_model,cols_date,rows,initiative_model

# Create your views here.
def bar_plots(request):
  labels = cols_date
  #data = base_model.loc['Traffic'].to_list()
  #labels = ['a','b']
  data = base_model.loc[rows[0]].to_list()

  base_model_html = base_model.to_html(table_id='base_model_data')
  initiative_model_html = initiative_model.to_html(table_id='initiative_model_data')

  return render(request, 'plots.html', {
    'labels': labels,
    'data': data,
    'base_model': base_model_html,
    'initiative_model': initiative_model_html,
  })
