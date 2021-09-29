import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input


app=dash.Dash()

app.layout=html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol'),
    dcc.Input(id='my_stock_pricker',
              value='TSLA'),
    dcc.Graph(id='my_graph',
              figure={'data':[{'x':[1,2],'y':[3,4]}],
                      'layout':{'title':'Default Title'}}
              )
])

@app.callback(Output('my_graph','figure'),
              [Input('my_stock_pricker','value')])
def update_figure(myVal):
    fig={'data':[{'x':[1,2],'y':[3,4]}],
         'layout':{'title':myVal}}
    return fig


if __name__=='__main__':
    app.run_server(debug=True)