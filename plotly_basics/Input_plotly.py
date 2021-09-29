import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

app=dash.Dash()

app.layout=html.Div([
    dcc.Input(id='my-id',
              value='Initial Text',
              type='text'),
    html.Div(id='my-div',
             style={'border':'2px blue solid'})
])

@app.callback(Output(component_id='my-div',component_property='children'),
              [Input(component_id='my-id',component_property='value')])

def update_output(my_input):
    return "The output: {}".format(my_input)

if __name__=="__main__":
    app.run_server(debug=True)