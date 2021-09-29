import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import json

df=pd.read_csv('mpg.csv')

# df['model_year']=1900+df['model_year']

df['model_year']=1900+df['model_year']+np.random.randint(-4,5,len(df))*0.1

# print(df['acceleration'])

app=dash.Dash()
app.layout=html.Div([
    html.Div([
        dcc.Graph(id='MPG-graph',
            figure={'data'  : [go.Scatter(x=df['model_year'],
                                                y=df['mpg'],
                                                text=df['name'],
                                                hoverinfo='text+y+x',
                                                mode='markers'
                                                )],
                          'layout': go.Layout(title='MPG Data',
                                              xaxis={'title': 'Model Year'},
                                              yaxis={'title': 'MPG'},
                                              hovermode='closest')
                          }
                  )
    ],style={'width':'50%','display':'inline-block'}),
    html.Div([dcc.Graph(id='my-mpg',
                        # figure={'data':[go.Scatter(x=[0,1],
                        #                            y=[0,1],
                        #                            mode='lines')],
                        #         'layout':go.Layout(
                        #             title='MPG Graph',
                        #             margin={'l':10}
                        #         )}
                        )],style={'width':'40%','display':'inline-block'}),
    html.Div([
        html.Pre(id='my-preview')
    ],style={'width':'50%','display':'inline-block'}),
    html.Div([
        dcc.Markdown(id='my-stats')
    ],style={'width':'48%','display':'inline-block','verticalAlign':'top'})
])

@app.callback(Output('my-stats','children'),
              [Input('MPG-graph','hoverData')])
def update_states(myHoverData):
    if myHoverData is None:
        return None
    else:
        dataIdx=myHoverData['points'][0]['pointIndex']
        stats="""
                {} cylinders
                {} cc displacement
                0 to 60mph in {} seconds
              """.format(df.iloc[dataIdx]['cylinders'],df.iloc[dataIdx]['displacement'],df.iloc[dataIdx]['mpg'])
        return stats



@app.callback(Output('my-preview','children'),
              [Input('MPG-graph','hoverData')])
def show_hoverData(myHoverData):
    if myHoverData is not None:
        dataIdx = myHoverData['points'][0]['pointIndex']
        return json.dumps(myHoverData,indent=2)+'\n'+str(60/df.iloc[dataIdx]['acceleration'])


@app.callback(Output('my-mpg','figure'),
              [Input('MPG-graph','hoverData')])
def update_graph(myHoverData):
    if myHoverData is not None:
        dataIdx=myHoverData['points'][0]['pointIndex']
        figure={'data':[go.Scatter(x=[0,1],
                                   y=[0,60/df.iloc[dataIdx]['acceleration']],
                                   mode='lines+markers',
                                   line={'width':2*df.iloc[dataIdx]['cylinders']}),
                        ],
                'layout':go.Layout(title=df.iloc[dataIdx]['name'],
                                   height=300,
                                   yaxis={'visible':False,'range':[0,60/df['acceleration'].min()]},
                                 )

            }
    else:
        figure = {'data':[go.Scatter(x=[0, 1],
                                        y=[0, 1],
                                        mode='lines')],
                  'layout': go.Layout(
                      title='MPG Graph',
                      margin={'l':3},
                      yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]},
                  )}
    return figure


if __name__=="__main__":
    app.run_server(debug=True)