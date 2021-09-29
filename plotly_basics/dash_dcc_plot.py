import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div([
    html.Label('Dropdown list'),
    dcc.Dropdown(options=[
        {'label':'New York City',
        'value':'NYC'},
        {'label':'San Francisco',
         'value':'SF'}],
        value='SF'),

    html.Label('Slider'),
    dcc.Slider(min=-10,
               max=10,
               step=0.5,
               marks={i:'{}'.format(i) for i in range(-10,10)},
               value=0),

    html.Label('Some radioitems'),
    dcc.RadioItems(options=[{'label':'New York City',
                             'value':'NYC'},
                            {'label':'San Francisco',
                             'value':'SF'}],
                   value='SF')

])

if __name__=='__main__':
    app.run_server(debug=True)