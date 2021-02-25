from django.db import models

from datetime import date
from time import strftime
import pandas as pd

# Create your models here.

start_date = date(2018,2,1)
end_date = date(2020,1,1)

cols_date = pd.date_range(start_date, end_date, freq='d', closed=None)
cols_date = cols_date[cols_date.day==1].strftime('%B %Y')

col1 = ['Funnel']
cols = col1 + cols_date.to_list()

df = pd.DataFrame(columns=cols)
df['Funnel'] = ['Traffic','Signup','Active','Conversion1','Payment']

base_model = df.copy()
