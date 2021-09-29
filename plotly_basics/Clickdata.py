import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64
import os
import json
import plotly.graph_objs as go

df=pd.read_csv('wheels.csv')

def encode_image(image_file):
    encoded=base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app=dash.Dash()

app.layout=html.Div([
    html.Div([dcc.Graph(id='my-graph',
              figure={'data':[go.Scatter(x=df['wheels'],
                                         y=df['color'],
                                         mode='markers',
                                         marker={'size':18},
                                         text=df['image'])],
                      'layout':go.Layout(title="wheel vs color",
                                         xaxis={'title':'Wheels'},
                                         yaxis={'title':'color'},
                                         hovermode='closest')})],style={'width':'30%','float':'left'}),
    html.Div([html.Img(id='my-img', src='children', height=300)],
             style={'width': '30%', 'display': 'inline-block'}),
    html.Br(),
    html.Div([html.Pre(id='my-output')],
             style={'width':'30%',
                    'float':'right',
                    'verticalAlign':'top',
                 })

])

@app.callback(Output('my-output','children'),
              [Input('my-graph','clickData')])
def show_clickData(myClickVal):
    return json.dumps(myClickVal,indent=2)


@app.callback(Output('my-img','src'),
              [Input('my-graph','clickData')])
def update_Image(myClickVal):
    if myClickVal==None:
        return None
    else:

        wheel=myClickVal['points'][0]['x']
        color=myClickVal['points'][0]['y']
        path=os.path.join(os.getcwd(),'images/')
        imageFile=df[(df['wheels']==wheel)&(df['color']==color)]['image'].values[0]
        return encode_image(path+imageFile)



if __name__=='__main__':
    app.run_server(debug=True)