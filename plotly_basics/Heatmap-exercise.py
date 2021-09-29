#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly import tools
import numpy as np

# Create a DataFrame from  "flights" data
df = pd.read_csv('flights.csv')

# Define a data variable
data=go.Heatmap(x=df['year'],
                 y=df['month'],
                 z=df['passengers'].values.tolist())


'my exercise heatmap'

# Define the layout
# fig=tools.make_subplots(rows=1,cols=1)
# fig.append_trace(data,1,1)
# fig['layout'].update(title='my exercise heatmap')
cols=len(df['year'])
rows=len(df['month'])

annotations=[]
for x,row in enumerate(df['month']):
    for y,col in enumerate(df['year']):
        v=df[(df.month==row)&(df.year==col)]['passengers'].values[0]
        annotation_dict=dict(
            showarrow=False,
            text='<b>'+str(v)+'<b>',
            xref='x',
            yref='y',
            x=x,
            y=y,
        )

        annotations.append(annotation_dict)


print(annotations)
#
layout=go.Layout(title='my exercise heatmap',
                 annotations=annotations)
fig=go.Figure(data=data,layout=layout)

# Create a fig from data and layout, and plot the fig
pyo.plot(fig,filename='my_Heatmap_exercise.html')