#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('2010YumaAZ.csv')

data=[go.Scatter(x=df[df.DAY==day]['LST_TIME'],
                 y=df[df.DAY==day]['T_HR_AVG'],
                 mode='lines+markers',
                 name=day) for day in df.DAY.unique()]
layout=go.Layout(title='my-line')

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='my-line.html')

