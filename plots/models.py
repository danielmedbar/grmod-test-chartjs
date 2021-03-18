from django.db import models

from datetime import date
from time import strftime
import pandas as pd

# Create your models here.

start_date = date(2020,1,1)
end_date = date(2021,5,1)

cols_date = pd.date_range(start_date, end_date, freq='d', closed=None)
cols_date = cols_date[cols_date.day==1].strftime('%B %Y').to_list()

rows = ['Traffic','Signup','Active','Conversion1','Payment']

import numpy as np
df = pd.DataFrame(data = np.random.randint(0,1000, size=(len(rows), len(cols_date))), columns = cols_date, index=rows)

row_i = 'Traffic'

base_model = df.copy().loc[[row_i]]
initiative_model = df.copy().loc[[row_i]]
