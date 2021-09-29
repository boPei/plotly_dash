import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Output, Input

df=pd.read_csv('mpg.csv')

app=dash.Dash()

app.layout=html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label':i,'value':i} for i in df.columns],
                     value='displacement')
    ],style={'width':'48%','display':'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label':i,'value':i} for i in df.columns],
                     value='mpg')
    ],style={'width':'48%','display':'inline-block'}),
    dcc.Graph(id='my-graph')
],style={'padding':10})

@app.callback(Output('my-graph','figure'),
              [Input('xaxis','value'),
               Input('yaxis','value')])
def update_figure(xvalue,yvalue):
    trace=[]
    trace.append(go.Scatter(x=df[xvalue],
                            y=df[yvalue],
                            mode='markers',
                            text=df['name'],
                            marker={'size':15,
                                    'opacity':0.5,
                                    'line':{'width':0.5,'color':'white'}}))

    return {'data':trace,
            'layout':go.Layout(title='My graph',
                               xaxis={'title':xvalue},
                               yaxis={'title':yvalue},
                               hovermode='closest')}



if __name__=="__main__":
    app.run_server(debug=True)