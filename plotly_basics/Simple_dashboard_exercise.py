#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go


# Launch the application:
app=dash.Dash()

# Create a DataFrame from the .csv file:
df=pd.read_csv('OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
app.layout=html.Div([
    dcc.Graph(
        id='My Scatter Plot',
        figure={'data':[go.Scatter(x=df['X'],
                                   y=df['Y'],
                                   mode='markers',
                                   marker={'color':'#2DEEFF'})],
                'layout':go.Layout(title='My Scatter Plot Exercise',
                                   xaxis={'title':'Eruption Duration'},
                                   yaxis={'title':'Waiting Time'})}
    )
])

if __name__ =="__main__":
    app.run_server(debug=True)




















# Add the server clause: