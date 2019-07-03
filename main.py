from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import app1, app2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/project':
         return app1.layout
    elif pathname == '/portfolio':
         return app2.layout
    else:
        return '404'

if __name__ == '__main__':
    #app.run_server(debug=True, host="0.0.0.0", port=80)
    app.run_server(debug=True, host='0.0.0.0', port=8080)
