import plotly.graph_objs as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

np.random.seed(42)
random_x=np.random.randn(500)
random_y=np.random.randn(500)

app=dash.Dash()

app.layout=html.Div([
    dcc.Graph(id='Scatter_Plot1',
              figure={'data':[go.Scatter(x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={'color':'#7EDFFE',
                                                 'size':12,
                                                 'symbol':'pentagon',
                                                 'line':{'width':2}})],
                      'layout':go.Layout(title='My First Scatter Plot',
                                         xaxis={'title':'some x title'})}),
    dcc.Graph(id='Scatter_Plot2',
              figure={'data'  : [go.Scatter(x=random_x,
                                            y=random_y,
                                            mode='markers',
                                            marker={'color' : '#8EDFDD',
                                                    'size'  : 12,
                                                    'symbol': 'pentagon',
                                                    'line'  : {'width': 2}})],
                      'layout': go.Layout(title='My Second Scatter Plot',
                                          xaxis={'title': 'some x title'})}),
])

if __name__=="__main__":
    app.run_server(debug=True)
