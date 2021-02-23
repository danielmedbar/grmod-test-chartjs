from django.urls import path
from . import views

urlpatterns = [
  path('', views.bar_plots, name='plots'),
]