import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import dash_auth

USERNAME_PASSWORD_PAIRS=[['username','password'],['boPei','peisel']]

app=dash.Dash()
auth=dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

app.layout=html.Div(
    [
        dcc.RangeSlider(id='range-slider',
                        max=10,
                        min=-10,
                        step=0.5,
                        value=[-5,5],
                        marks={i:'{}'.format(i) for i in range(-10,11)}),
        html.H1(id='my-output')
    ]
)
@app.callback(Output('my-output','children'),
              Input('range-slider','value'))
def update_output(myVal):
    return '{}'.format(myVal[0]*myVal[1])


if __name__=='__main__':
    app.run_server()