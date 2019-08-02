from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

from app import app
from apps.fn_jira import get_portfolio_mapping, get_portfolios, get_subportfolios, get_projects, get_issue_active_sprint, get_project_details


def generate_table(dataframe, max_rows=10,html_class='col-sm-6'):
    return html.Div(className=html_class, children=html.Table(
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    , className='table table-condensed'))

layout = html.Div([
            html.Div(style={'height':56},children=[
                html.Div(className='col-sm-2', children=[
                    html.Img(src='https://hycpms.ril.com/s/z431h9/712001/71d43a18\
                        f6924bb6567625cfc3d9faf9/_/jira-logo-scaled.png',
                        style={'float':'left','height':26,'position':'absolute','top': 7,'left': 10}
                    )]
                ),
                html.Div(html.H3('Project Dashboard',style={'textAlign':'center'}),className='col-sm-6'),
                html.Div(dcc.Link('Portfolio Dashboard',href='/portfolio'), style={'margin-top': 20, 'margin-bottom': 20}, className='col-sm-4')
            ]),
    dcc.Dropdown(id='portfolio_dd', className='col-sm-4',
        options=[
            {'label': row['displayName'], 'value': row['id'] } for index,row in get_portfolios().iterrows() 
        ]
    ),
    dcc.Dropdown(id='subportfolio_dd', className='col-sm-4'),
    dcc.Dropdown(id='project_dd', className='col-sm-4'),
    html.Div(id='project_table', className='col-sm-12',style={'marginTop':20}),
    html.Div(id='app-1-display-value')
])


@app.callback(
        Output('subportfolio_dd', 'options'),
        [Input('portfolio_dd','value')])
def subportfolio_dd(value):
    options= [{'label':row['displayName'], 'value':row['id']} for index,row in get_subportfolios(value).iterrows()]
    return options

@app.callback(
       Output('project_dd','options'),
        [Input('portfolio_dd','value'),
        Input('subportfolio_dd','value')])
def project_dd(portfolio,subportfolio):
    df=get_portfolio_mapping()
    one = df[df['id']==portfolio]['code'].iloc[0] if portfolio else ''
    two = df[df['id']==subportfolio]['code'].iloc[0] if subportfolio else ''
    project_list = get_projects(one,two)
    return [{'label':project_list.iloc[i]['project']+' - '+project_list.iloc[i]['projectname'] , 'value':project_list.iloc[i]['project']} for i in range(len(project_list))]

@app.callback(
        Output('project_dd','value'),
        [Input('portfolio_dd','value'),
            Input('subportfolio_dd','value')])
def reset_pro_dd(port,subport):
    return ''

@app.callback(
        Output('subportfolio_dd','value'),
        [Input('portfolio_dd','value')])
def reset_subplat_dd(port):
    return ''


@app.callback(
        Output('project_table','children'),
        [Input('project_dd','value'),
         Input('subportfolio_dd','value'),
         Input('portfolio_dd','value')],
        [State('project_dd','value')])
def project_table(project_id,sub,port,s_project_id):
    issue_table=html.Div('')
    test= html.Div('')
    issue_type=html.Div('')
    if project_id:
        issues, issue_type_count, issue_status_count = get_project_details(project_id)
        test = generate_table(issue_type_count[['Issue Type','Issue Count']],20,html_class='col-sm-2')
        issue_type = generate_table(issue_status_count[['Status Type','Issue Count']],max_rows=10,html_class='col-sm-2')
        issue_table = generate_table(issues,60,html_class='col-sm-12')        
        return (test,issue_type,issue_table)
    if sub:
        return html.Div('Sub-Protrolio Selected')
    if port:
        
        return html.Div('Portfolio Selected')
    portfolios=generate_table(get_portfolio_mapping().rename(columns={'displayName':'Portfolio','id':'ID'}))
    return (portfolios)
        

