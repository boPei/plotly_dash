import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import numpy as np
import plotly.graph_objs as go
import pandas as pd
import json


np.random.seed(42)
x1=np.linspace(0.1,5,50)
x2=np.linspace(5.1,10,50)
y=np.random.randint(0,50,50)

df1=pd.DataFrame({'x':x1,'y':y})
df2=pd.DataFrame({'x':x1,'y':y})
df3=pd.DataFrame({'x':x2,'y':y})

df=pd.concat([df1,df2,df3])

app=dash.Dash()
app.layout=html.Div([
    html.Div([dcc.Graph(id='my-graph',
                        figure={'data':[go.Scatter(x=df['x'],
                                                   y=df['y'],
                                                   mode='markers',
                                                   marker={'opacity':0.75},
                                                   line={'width':1,'color':'blue'})],
                                'layout':go.Layout(title='My density calculation plot',
                                                   xaxis={'title':'X'},
                                                   yaxis={'title':'Y'},
                                                   hovermode='closest')})],
             style={'width':'30%','float':'left'}),
    html.Div([html.H1(id='my-output')],
             style={'width':'30%','display':'inline-block'}),
    html.Div([html.Pre(id='my-pre')],
             style={'width':'30%','float':'right'})
])
@app.callback(Output('my-pre','children'),
              [Input('my-graph','selectedData')])
def show_dataSelected(mySelected):
    return json.dumps(mySelected,indent=2)


@app.callback(Output('my-output','children'),
              [Input('my-graph','selectedData')])
def find_density(mySelected):
    if mySelected==None:
        return None
    else:
        dataLen=len(mySelected['points'])
        dictIdx=list(mySelected.keys())
        dictIdx.remove('points')
        min_x=min(mySelected[dictIdx[0]]['x'])
        max_x=max(mySelected[dictIdx[0]]['x'])
        #
        min_y=min(mySelected[dictIdx[0]]['y'])
        max_y=max(mySelected[dictIdx[0]]['y'])

        area=(max_x-min_x)*(max_y-min_y)
        d=round(dataLen/area,3)

        return str(d)

if __name__=='__main__':
    app.run_server(debug=True)