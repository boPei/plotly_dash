"""
1. Import boilerplate
"""
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


"""
2. Instantiate the app
"""
# app=dash.Dash(__name__)
# app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
# app=dash.Dash(__name__,external_stylesheets=[dbc.themes.SUPERHERO])
# app=dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.MINTY])
"""
3. Layout
"""
# app.layout=html.Div([html.H1('Hello World'),
#                      html.H2('A blue title',
#                              style={"color":'blue',
#                                     "fontSize":'14px',
#                                     "marginLeft":'20%'})])

app.layout=html.Div([html.H1('Poverty And Equity Database',
                             style={"color":'blue',
                                    "fontSize":'40px'}),
                     html.H2('The World Bank'),
                     html.P('Key Facts:'),
                     html.Ul([html.Li('Number of Economies: 170'),
                              html.Li('Temporal Coverage: 1974-2019'),
                              html.Li('Update Frequency: Quarterly'),
                              html.Li('Last Updated: March 18,2020'),
                              html.Li(['Source:',
                                      html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                                      href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')])])
                     ])

"""
4. callback
    None
"""

"""
5. running the app
"""
if  __name__=='__main__':
    app.run_server(debug=True)