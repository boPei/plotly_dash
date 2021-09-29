import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df=pd.read_csv('mpg.csv')

df['model_year']=1900+df['model_year']

# df['model_year']=1900+df['model_year']+np.random.randint(-4,5,len(df))*0.1


app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(figure={'data':[ go.Scatter(x=df['model_year'],
               y=df['mpg'],
               text=df['name'],
               hoverinfo='text+y+x',
               mode='markers'
               )],
                      'layout':go.Layout(title='MPG Data',
                                         xaxis={'title':'Model Year'},
                                         yaxis={'title':'MPG'},
                                         hovermode='closest')
                      })

])


if __name__=="__main__":
    app.run_server(debug=True)