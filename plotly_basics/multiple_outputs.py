import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import base64
import os

#
# path=os.path.join(os.getcwd(),'images')
# print(path)
#

def encode_image(image_file):
    encoded=base64.b64encode(open(image_file,'rb').read())
    return "data:image/png;base64,{}".format(encoded.decode())

df=pd.read_csv('wheels.csv')
app=dash.Dash()
app.layout=html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label':i,'value':i} for i in df['wheels'].unique()],
                   value=1),
    html.Div(id='wheel-output'),
    html.Hr(),
    dcc.RadioItems(id='color',
                   options=[{'label':i,'value':i} for i in df['color'].unique()],
                   value='red'),
    html.Div(id='color-output'),
    html.Img(id='my-img',src='children',height=300)
],style={'fontFamily':'helvetica',
         'fontSize':18})


@app.callback(Output('wheel-output','children'),
              [Input('wheels','value')])
def display_wheels(my_wheel):
    return 'Your selected wheel is {}'.format(my_wheel)

@app.callback(Output('color-output','children'),
              [Input('color','value')])
def display_color(my_color):
    return "Your selected color is {}".format(my_color)

@app.callback(Output('my-img','src'),
              [Input('wheels','value'),
               Input('color','value')])
def display_images(my_wheel,my_color):
    path=os.path.join(os.getcwd(),'images\/')
    return encode_image(path+df[(df['wheels']==my_wheel)&(df['color']==my_color)]['image'].values[0])

if __name__=='__main__':
    app.run_server(debug=True)

