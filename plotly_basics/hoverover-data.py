import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd
import json
import os
import base64


def encode_image(image_file):
    encoded=base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

df=pd.read_csv('wheels.csv')

app=dash.Dash()

app.layout=html.Div(
    [
        html.Div(dcc.Graph(id='wheels-plot',
                           figure={'data':[go.Scatter(x=df['color'],
                                                      y=df['wheels'],
                                                      dy=1,
                                                      mode='markers',
                                                      marker={'size':18})],
                                   'layout':go.Layout(title='Test',
                                                      hovermode='closest'),
                                   },
                           ),style={'width':'48%','float':'left'}),
        html.Div(html.Pre(id='hover-data',style={'paddingTop':32}),
                 style={'width':'30%'}),
        html.Img(id='my-img',
                 src='children',
                 height=300,
                 style={'float':'right','paddingTop':35})
    ]
)

@app.callback(Output('hover-data','children'),
              [Input('wheels-plot','hoverData')])
def update_data(hoverData):
    return json.dumps(hoverData,indent=2)


@app.callback(Output('my-img','src'),
              [Input('wheels-plot','hoverData')])
def update_image(myData):
    if myData==None:
        return None
    else:

        color=myData['points'][0]['x']
        wheels=myData['points'][0]['y']
        path=os.path.join(os.getcwd(),'images/')

        return encode_image(path+df[(df['wheels']==wheels)&(df['color']==color)]['image'].values[0])


if __name__=='__main__':
    app.run_server(debug=True)