#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df=pd.read_csv('abalone.csv')

# take two random samples of different sizes:
rnd_ring1=np.random.choice(df['rings'],50,replace=False)
rnd_ring2=np.random.choice(df['rings'],60,replace=False)

rnd_sex=np.random.choice(df['sex'],50,replace=False)

# create a data variable with two Box plots:
# data=[go.Box(x=rnd_sex,
#                 y=rnd_ring)]
data=[go.Box(y=rnd_ring1,name='first sample'),
      go.Box(y=rnd_ring2,name='second sample')]



# add a layout
layout=go.Layout(title='boxplot exercise')

# create a fig from data & layout, and plot the fig
fig=go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='boxplot.html')