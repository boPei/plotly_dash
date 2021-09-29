import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input,Output


df=pd.read_csv('gapminderDataFiveYear.csv')

year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year),
                         'value':year})

app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
                 options=year_options,
                 value=df['year'].min())
])

@app.callback(Output('graph',
                     'figure'),
              [Input('year-picker',
                     'value')])
def update_figure(selected_year):
    filtered_df=df[df['year']==selected_year]
    trace=[]
    for continent in filtered_df['continent'].unique():
        trace.append(go.Scatter(x=filtered_df[filtered_df.continent==continent]['gdpPercap'],
                               y=filtered_df[filtered_df.continent==continent]['lifeExp'],
                               mode='markers',
                               marker={'size':12},
                               name=continent))

    return {'data':trace,
            'layout':go.Layout(title='GDP VS LifeExp',
                               xaxis={'title':'GDP per Cap','type':'log'},
                               yaxis={'title':'Life Expectancy'})}

if __name__=='__main__':
    app.run_server(debug=True)