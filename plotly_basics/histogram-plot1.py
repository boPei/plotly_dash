import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df=pd.read_csv('mpg.csv')
#data=[go.Histogram(x=df['mpg'])]
# edit the bin size for the dataset
data=[go.Histogram(x=df['mpg'],xbins=dict(start=0,end=50,size=2))]


layout=go.Layout(title='Histogram')

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='histogram.html')