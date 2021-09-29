#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd




# create a DataFrame from the .csv file:
df=pd.read_csv('mocksurvey.csv')
df.set_index('index',inplace=True)
print(df.head())
# create traces using a list comprehension:

trace=[go.Bar(x=df.index,
              y=df[response]) for response in df.columns]



# create a layout, remember to set the barmode here
layout=go.Layout(title='my exercise bar chart')



# create a fig from data & layout, and plot the fig.
fig=go.Figure(data=trace,layout=layout)
pyo.plot(fig)