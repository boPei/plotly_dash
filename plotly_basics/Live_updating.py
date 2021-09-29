import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc


app=dash.Dash()


crash_free=0

def update_refresh():
    global crash_free
    crash_free+=1
    return html.H1('Crash free for {} refreshers'.format(crash_free))

app.layout=update_refresh

if __name__=='__main__':
    print(crash_free)
    app.run_server()