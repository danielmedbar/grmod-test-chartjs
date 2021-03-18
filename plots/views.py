from django.shortcuts import render
from django.http import HttpResponse

from .models import base_model,cols_date,rows,initiative_model,row_i

# Create your views here.
def bar_plots(request):
  labels = cols_date
  row_name = row_i

  base_model_values = base_model.iloc[0].tolist()
  initiative_model_values = initiative_model.iloc[0].tolist()

  base_model_html = base_model.to_html(table_id='base_model_data')
  initiative_model_html = initiative_model.to_html()

  return render(request, 'plots.html', {
    'labels': labels,
    'row_name': row_name,

    
    'base_model': base_model_html,
    'initiative_model': initiative_model_html,
    
    'base_model_values': base_model_values,
    'initiative_model_values': initiative_model_values,

  })
