import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css','https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
