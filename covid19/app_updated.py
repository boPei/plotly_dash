import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG]
)
server=app.server
app.title='Manufacturing SPC Dashboard'
app.config['suppress_callback_exceptions']=True

def build_banner(app):
    title=html.H5('Manufacturing SPC Dashboard',
                  style={'marginTop':5,
                         'marginLeft':'10px'})
    info_about_app=html.H6('Process Control and Exception Reporting',
                           style={'marginLeft':'10px'})
    learn_about_btn=html.Button('Learn More',
                                style={'textTransform':'uppercase',
                                       'marginTop':5
                                       })
    logo_image=html.Img(
        src=app.get_asset_url('plotly_logo.png'),
        style={'float':'right',
               'height':50}
    )
    link=html.A(logo_image,
                href="https://plotly.com")
    return dbc.Row([dbc.Col([dbc.Row([title]),
                            dbc.Row([info_about_app])
                            ]),
                   dbc.Col([learn_about_btn]),
                   dbc.Col([link])]
                   )






app.layout=dbc.Container(
    fluid=True,
    children=[build_banner(app)]
)

if __name__=="__main__":
    app.run_server(debug=True,port=8051)