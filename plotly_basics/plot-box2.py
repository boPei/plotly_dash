import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data=[go.Box(y=snodgrass,name='QCS'),
      go.Box(y=twain,name='MT')]

layout=go.Layout(title='Comparison of three-letter-word frequencies<br>  between Quintus Curtius Snodgrass and Mark Twain')

fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='box3.html')