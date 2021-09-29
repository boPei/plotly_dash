import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df=pd.read_csv('arrhythmia.csv')

data=[go.Histogram(x=df[df.Sex==1]['Height'],
                   name='female',
                   opacity=0.65),
      go.Histogram(x=df[df.Sex==0]['Height'],
                   name='male',
                   opacity=0.75)]

layout=go.Layout(title='My Histogram2')
fig=go.Figure(data=data,layout=layout)

pyo.plot(fig)