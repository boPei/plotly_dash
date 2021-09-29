import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

app=dash.Dash()

app.layout=html.Div([
    html.H1(id='my-output'),
    dcc.Interval(id='my-interval',
                 interval=2000,
                 n_intervals=0)
])

@app.callback(Output('my-output','children'),
              [Input('my-interval','n_intervals')])
def update_refresher(n_interval):
    return "There are {} refreshers".format(n_interval)


if __name__=='__main__':
    app.run_server()