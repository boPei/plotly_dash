import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

app=dash.Dash()

app.layout=html.Div([
    dcc.RangeSlider(id='my-rangeSlider',
                    min=-5,
                    max=6,
                    step=0.5,
                    value=[-5,5],
                    marks={i:'{}'.format(i) for i in range(-5,7)}),
    html.Div(id='my-output',
             style={'size':18})
])

@app.callback(Output('my-output','children'),
              [Input('my-rangeSlider','value')])
def update_Output(inputVal):
    return inputVal[0]*inputVal[1]

if __name__=='__main__':
    app.run_server(debug=True)