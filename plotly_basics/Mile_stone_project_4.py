import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input,State
import pandas_datareader.data as web
from datetime import datetime
import os


app=dash.Dash()

app.layout=html.Div([
    html.H1('Stock Ticker Dashboard'),

    html.Div([
        html.H3('Enter a stock symbol',
                style={'paddingRight':'30px'}),

        dcc.Input(id='my_stock_pricker',
                value='TSLA',
                style={'fontSize':24,'width':75})],style={'display':'inline-block','verticalAlign':'top'}),
    html.Div([
        html.H3('Select a start and end date'),
        dcc.DatePickerRange(id='my_date_picker',
                            min_date_allowed=datetime(2015,1,1),
                            max_date_allowed=datetime.today(),
                            start_date=datetime(2018,1,1),
                            end_date=datetime.today()),
        html.Button(id='my-btn',
                    n_clicks=0,
                    children='Submit',
                    style={'fontSize': 24,
                           'paddingLeft':'30px',
                           'paddingRight':'30px',
                           'paddingTop':'5px',
                           'paddingBottom':'12px',
                           'marginLeft':20}),
    ],style={'display':'inline-block'}),


    dcc.Graph(id='my_graph',
              figure={'data':[{'x':[1,2],'y':[3,4]}],
                      'layout':{'title':'Default Title'}}
              ),
    html.Div(id='my-output')
])


@app.callback(Output('my_graph','figure'),
              [Input('my-btn','n_clicks')],
              [State('my_stock_pricker','value'),
               State('my_date_picker','start_date'),
               State('my_date_picker','end_date')])
def update_figure(n_clicks,myVal,startDate,endDate):

    start=datetime.strftime(datetime.strptime(startDate[:10],'%Y-%m-%d'),'%Y-%m-%d')
    end=datetime.strftime(datetime.strptime(endDate[:10],'%Y-%m-%d'),'%Y-%m-%d')

    os.environ["ALPHAVANTAGE_API_KEY"] = "30YR5UBCWX916WKU"
    df = web.DataReader(myVal, 'av-daily', start, end)
    fig={'data':[{'x':df.index,'y':df.close}],
         'layout':{'title':myVal}}

    return fig



if __name__=='__main__':
    app.run_server(debug=True)

