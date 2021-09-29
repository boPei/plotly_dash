#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.figure_factory as ff
import plotly.offline as pyo
import pandas as pd


# create a DataFrame from the .csv file:
df=pd.read_csv('iris.csv')

# Define the traces
Iris_Length=[df[df['class']=='Iris-setosa']['petal_length'],
             df[df['class']=='Iris-versicolor']['petal_length'],
             df[df['class']=='Iris-virginica']['petal_length']]

group_labels=['Iris-setosa','Iris-versicolor','Iris-virginica']


# HINT:
# This grabs the petal_length column for a particular flower

data=ff.create_distplot(Iris_Length,group_labels,bin_size=[0.05,0.05,0.05])

pyo.plot(data)

# Define a data variable



# Create a fig from data and layout, and plot the fig