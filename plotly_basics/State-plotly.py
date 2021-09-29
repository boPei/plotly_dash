import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State

app=dash.Dash()

app.layout=html.Div(
    [
        dcc.Input(id='my-input',
                  value=1,
                  style={'size':18}),
        html.Button('Submit',id='my-btn',
                    n_clicks=0),
        html.H1(id='my-output')
    ]
)

@app.callback(Output('my-output','children'),
              [Input('my-btn','n_clicks')],
              State('my-input','value'))

def updated_output(myClick,myVal):
    return 'The number of clicks {} and the value in input box is {}'.format(myClick,myVal)

if __name__=='__main__':
    app.run_server(debug=True)