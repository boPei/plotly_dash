import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import requests
import plotly.graph_objs as go

app=dash.Dash()

app.layout=html.Div([
    html.Div([
        html.Iframe(src='https://www.flightradar24.com',
                    height=500,width=1200)
    ]),
    html.Div([
        html.Pre(id='counter_text',
                 children='Active Flights Worldwid'),
        dcc.Graph(id='my-graph'),
        dcc.Interval(id='interactive-component',
                     interval=6000,
                     n_intervals=0)
    ])
])
counter_list=[]
@app.callback(Output('counter_text','children'),
              [Input('interactive-component','n_intervals')])
def update_layout(n_interval):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
       &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    res = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    data = res.json()
    counter=0

    for element in data['stats']['total']:
        counter+=data['stats']['total'][element]
        counter_list.append(counter)
    return 'Active flights worldWide: {}'.format(counter)


@app.callback(Output('my-graph','figure'),
              [Input('interactive-component','n_intervals')])
def update_gaph(n_intervals):
    figure={'data':[go.Scatter(x=list(range(len(counter_list))),
                       y=counter_list,
                       mode='lines+markers')]}
    return figure



if __name__=='__main__':
    app.run_server(debug=True)