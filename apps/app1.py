import yaml
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

from jira import JIRA
from app import app

with open("conf.yml","r") as yml_file:
    config = yaml.load(yml_file)

jira_s = JIRA(config['jira_site'], auth=(config['user'],config['pass']))

def get_portfolio_mapping():
#    import requests
#    import json
#    import pandas as pd
#    r=requests.get("http://10.21.193.59/rfabric/getplatformservice/getallplatforms")
    r=pd.DataFrame([{"id":1,"name":"hr","displayName":"HR","parentId":0,"code":"hr","serialNum":"000","gitlabId":100},{"id":3,"name":"om","displayName":"OM, Hire and Onboard","parentId":1,"code":"om","serialNum":"014","gitlabId":0},{"id":7,"name":"om","displayName":"OM, Hire and Onboard","parentId":3,"code":"om","serialNum":"000","gitlabId":0},{"id":9,"name":"corporatesecurity","displayName":"Corporate Security","parentId":0,"code":"SE","serialNum":"000","gitlabId":107},{"id":11,"name":"accesscontrol","displayName":"Access Control","parentId":9,"code":"AC","serialNum":"000","gitlabId":0},{"id":13,"name":"accesscontrol","displayName":"Access Control","parentId":11,"code":"AC","serialNum":"000","gitlabId":0},{"id":15,"name":"surveillance","displayName":"Surveillance ","parentId":9,"code":"SU","serialNum":"000","gitlabId":0},{"id":17,"name":"surveillance","displayName":"Surveillance ","parentId":15,"code":"SU","serialNum":"000","gitlabId":0},{"id":19,"name":"intelligence","displayName":"Intelligence ","parentId":9,"code":"IN","serialNum":"000","gitlabId":0},{"id":21,"name":"intelligence","displayName":"Intelligence ","parentId":19,"code":"IN","serialNum":"000","gitlabId":0},{"id":23,"name":"securityoperationscenter","displayName":"Security Operations Center","parentId":9,"code":"SO","serialNum":"000","gitlabId":0},{"id":25,"name":"securityoperationscenter","displayName":"Security Operations Center","parentId":23,"code":"SO","serialNum":"000","gitlabId":0},{"id":27,"name":"engagealignperform","displayName":"Engage, Align and Perform","parentId":1,"code":"EP","serialNum":"000","gitlabId":0},{"id":29,"name":"engagealignperform","displayName":"Engage, Align and Perform","parentId":27,"code":"EP","serialNum":"000","gitlabId":0},{"id":31,"name":"learnandgrow","displayName":"Learn and Grow","parentId":1,"code":"LG","serialNum":"000","gitlabId":0},{"id":33,"name":"learnandgrow","displayName":"Learn and Grow","parentId":31,"code":"LG","serialNum":"000","gitlabId":0},{"id":35,"name":"rewardandrecognize","displayName":"Reward and Recognize","parentId":1,"code":"RR","serialNum":"000","gitlabId":0},{"id":37,"name":"rewardandrecognize","displayName":"Reward and Recognize","parentId":35,"code":"RR","serialNum":"000","gitlabId":0},{"id":39,"name":"leadandexcel","displayName":"Lead and Excel","parentId":1,"code":"LE","serialNum":"000","gitlabId":0},{"id":41,"name":"leadandexcel","displayName":"Lead and Excel","parentId":37,"code":"LE","serialNum":"000","gitlabId":0},{"id":43,"name":"employeeservices","displayName":"Employee Services","parentId":1,"code":"ES","serialNum":"000","gitlabId":0},{"id":45,"name":"employeeservices","displayName":"Employee Services","parentId":43,"code":"ES","serialNum":"000","gitlabId":0},{"id":47,"name":"corporateservices","displayName":"Corporate Services","parentId":0,"code":"CS","serialNum":"000","gitlabId":108},{"id":49,"name":"foodandbeverages","displayName":"Food and Beverages","parentId":47,"code":"FB","serialNum":"000","gitlabId":0},{"id":51,"name":"foodandbeverages","displayName":"Food and Beverages","parentId":49,"code":"FB","serialNum":"000","gitlabId":0},{"id":53,"name":"realestatemanagement","displayName":"Real Estate Management / Housing","parentId":47,"code":"RH","serialNum":"000","gitlabId":0},{"id":55,"name":"realestatemanagement","displayName":"Real Estate Management / Housing","parentId":53,"code":"RH","serialNum":"000","gitlabId":0},{"id":57,"name":"transitaccommodation","displayName":"Transit Accommodation Services","parentId":47,"code":"TA","serialNum":"000","gitlabId":0},{"id":59,"name":"transitaccommodation","displayName":"Transit Accommodation Services","parentId":57,"code":"TA","serialNum":"000","gitlabId":0},{"id":61,"name":"travel","displayName":"Travel","parentId":47,"code":"TR","serialNum":"001","gitlabId":0},{"id":63,"name":"travel","displayName":"Travel","parentId":61,"code":"TR","serialNum":"000","gitlabId":0},{"id":65,"name":"liaison","displayName":"Liaison","parentId":47,"code":"LI","serialNum":"000","gitlabId":0},{"id":67,"name":"liaison","displayName":"Liaison","parentId":65,"code":"LI","serialNum":"000","gitlabId":0},{"id":69,"name":"facilities","displayName":"Facilities Management","parentId":47,"code":"FM","serialNum":"000","gitlabId":0},{"id":71,"name":"facilities","displayName":"Facilities Management","parentId":69,"code":"FM","serialNum":"000","gitlabId":0},{"id":73,"name":"office","displayName":"Office Services","parentId":47,"code":"OS","serialNum":"000","gitlabId":0},{"id":75,"name":"office","displayName":"Office Services","parentId":73,"code":"OS","serialNum":"000","gitlabId":0},{"id":77,"name":"medical","displayName":"Medical","parentId":0,"code":"MD","serialNum":"000","gitlabId":109},{"id":79,"name":"hospitalmanagement","displayName":"Hospital Management","parentId":77,"code":"HM","serialNum":"000","gitlabId":0},{"id":81,"name":"hospitalmanagement","displayName":"Hospital Management","parentId":79,"code":"HM","serialNum":"000","gitlabId":0},{"id":83,"name":"occupationalhealth","displayName":"Occupational Health","parentId":77,"code":"OH","serialNum":"000","gitlabId":0},{"id":85,"name":"occupationalhealth","displayName":"Occupational Health","parentId":83,"code":"OH","serialNum":"000","gitlabId":0},{"id":87,"name":"employeehealth","displayName":"Employee Health Management","parentId":77,"code":"EH","serialNum":"000","gitlabId":0},{"id":89,"name":"employeehealth","displayName":"Employee Health Management","parentId":87,"code":"EH","serialNum":"000","gitlabId":0},{"id":91,"name":"manufacturing","displayName":"Manufacturing","parentId":0,"code":"MF","serialNum":"000","gitlabId":110},{"id":93,"name":"operationsmaintenance","displayName":"Operations & Maintenance","parentId":91,"code":"OP","serialNum":"000","gitlabId":0},{"id":95,"name":"operationsmaintenance","displayName":"Operations & Maintenance","parentId":93,"code":"OP","serialNum":"000","gitlabId":0},{"id":97,"name":"technicalservices","displayName":"Technical Services","parentId":91,"code":"TS","serialNum":"000","gitlabId":0},{"id":99,"name":"technicalservices","displayName":"Technical Services","parentId":97,"code":"TS","serialNum":"000","gitlabId":0},{"id":101,"name":"reliability","displayName":"Reliability","parentId":91,"code":"RE","serialNum":"000","gitlabId":0},{"id":103,"name":"reliability","displayName":"Reliability","parentId":101,"code":"RE","serialNum":"000","gitlabId":0},{"id":105,"name":"hsef","displayName":"HSEF","parentId":91,"code":"HS","serialNum":"000","gitlabId":0},{"id":107,"name":"hsef","displayName":"HSEF","parentId":105,"code":"HS","serialNum":"000","gitlabId":0},{"id":109,"name":"rpmg","displayName":"RPMG","parentId":91,"code":"RP","serialNum":"000","gitlabId":0},{"id":111,"name":"rpmg","displayName":"RPMG","parentId":109,"code":"RP","serialNum":"000","gitlabId":0},{"id":113,"name":"rd","displayName":"R&D","parentId":91,"code":"RD","serialNum":"000","gitlabId":0},{"id":115,"name":"rd","displayName":"R&D","parentId":113,"code":"RD","serialNum":"000","gitlabId":0},{"id":117,"name":"refiningnmarketing","displayName":"Refining & Marketing","parentId":0,"code":"RM","serialNum":"000","gitlabId":126},{"id":119,"name":"marketing","displayName":"marketing","parentId":117,"code":"MK","serialNum":"003","gitlabId":0},{"id":121,"name":"aviation","displayName":"Aviation","parentId":119,"code":"AV","serialNum":"000","gitlabId":0},{"id":123,"name":"petroretail","displayName":"Petro Retail","parentId":119,"code":"PR","serialNum":"000","gitlabId":0},{"id":125,"name":"centralit","displayName":"Central IT","parentId":0,"code":"CE","serialNum":"000","gitlabId":141},{"id":127,"name":"centralit","displayName":"Central IT","parentId":125,"code":"CE","serialNum":"008","gitlabId":0},{"id":129,"name":"centralit","displayName":"Central IT","parentId":127,"code":"CE","serialNum":"000","gitlabId":0},{"id":130,"name":"procurementcontracting","displayName":"Procurement & Contracting","parentId":0,"code":"PC","serialNum":"000","gitlabId":170},{"id":132,"name":"financialmanagementservices","displayName":"Financial Management Services","parentId":0,"code":"FM","serialNum":"000","gitlabId":171},{"id":134,"name":"petchem","displayName":"Petchem","parentId":0,"code":"PC","serialNum":"000","gitlabId":17},{"id":136,"name":"categorymanagement","displayName":"Category Management","parentId":130,"code":"CM","serialNum":"000","gitlabId":0},{"id":138,"name":"intelligentesourcing","displayName":"Intelligent E-Sourcing","parentId":130,"code":"IE","serialNum":"000","gitlabId":0},{"id":140,"name":"fulfilmentmanagement","displayName":"Fulfilment Management","parentId":130,"code":"FM","serialNum":"000","gitlabId":0},{"id":142,"name":"logisticscontroltower","displayName":"Logistics Control Tower","parentId":130,"code":"LC","serialNum":"000","gitlabId":0},{"id":144,"name":"materialsmanagement","displayName":"Materials Management","parentId":130,"code":"MM","serialNum":"001","gitlabId":0},{"id":146,"name":"contractorlifecyclemanagement","displayName":"Contractor Lifecycle Management","parentId":130,"code":"CM","serialNum":"000","gitlabId":0},{"id":148,"name":"suppliersupport","displayName":"Supplier Support","parentId":130,"code":"SS","serialNum":"000","gitlabId":0},{"id":150,"name":"workingcapitalmanagement","displayName":"Working Capital Management","parentId":130,"code":"WM","serialNum":"000","gitlabId":0},{"id":152,"name":"servicesfcaplatform","displayName":"Services from FC&A platform","parentId":130,"code":"SF","serialNum":"000","gitlabId":0},{"id":154,"name":"treasury","displayName":"Treasury","parentId":132,"code":"TR","serialNum":"000","gitlabId":0},{"id":156,"name":"insurance","displayName":"Insurance","parentId":132,"code":"IN","serialNum":"000","gitlabId":0},{"id":158,"name":"directtaxes","displayName":"Direct Taxes","parentId":132,"code":"DT","serialNum":"001","gitlabId":0},{"id":160,"name":"indirecttaxes","displayName":"Indirect Taxes","parentId":132,"code":"ID","serialNum":"000","gitlabId":0},{"id":162,"name":"corporatesecretarial","displayName":"Corporate Secretarial","parentId":132,"code":"CS","serialNum":"000","gitlabId":0},{"id":164,"name":"consolidation","displayName":"Consolidation","parentId":132,"code":"CO","serialNum":"000","gitlabId":0},{"id":166,"name":"planningperformancemgmt","displayName":"Planning & Performance Mgmt.","parentId":132,"code":"PL","serialNum":"000","gitlabId":0},{"id":168,"name":"procuretopay","displayName":"Procure-to-Pay (Accounts Payable)","parentId":132,"code":"AP","serialNum":"001","gitlabId":0},{"id":170,"name":"ordertocash","displayName":"Order-to-Cash (Accounts Receivable)","parentId":132,"code":"AR","serialNum":"000","gitlabId":0},{"id":172,"name":"commissioningtoobsolescence","displayName":"Commissioning-to-Obsolescence(Asset Accounting)","parentId":132,"code":"AA","serialNum":"000","gitlabId":0},{"id":174,"name":"projectaccounting","displayName":"Project Accounting","parentId":132,"code":"PA","serialNum":"000","gitlabId":0},{"id":176,"name":"hiretoretire","displayName":"Hire-to-Retire (Payroll/ Benefits)","parentId":132,"code":"HR","serialNum":"000","gitlabId":0},{"id":178,"name":"marketingevents","displayName":"Marketing & Events","parentId":134,"code":"ME","serialNum":"000","gitlabId":0},{"id":180,"name":"fieldcrm","displayName":"Field & CRM","parentId":134,"code":"FC","serialNum":"000","gitlabId":0},{"id":182,"name":"saleschannel","displayName":"Sales & Channel","parentId":134,"code":"SC","serialNum":"000","gitlabId":0},{"id":184,"name":"businessplanningoptimization","displayName":"Business Planning & Optimization","parentId":134,"code":"BP","serialNum":"000","gitlabId":0},{"id":186,"name":"logistics","displayName":"Logistics","parentId":134,"code":"LO","serialNum":"000","gitlabId":0},{"id":188,"name":"enterpriseitinfra","displayName":"Enterprise IT Infra","parentId":125,"code":"IN","serialNum":"000","gitlabId":0},{"id":190,"name":"collaborationintegration","displayName":"Collaboration and Integration","parentId":188,"code":"CI","serialNum":"000","gitlabId":0},{"id":192,"name":"idcnetworksecurity","displayName":"IDC Network and Security","parentId":188,"code":"NS","serialNum":"000","gitlabId":0},{"id":194,"name":"idcstoragehosting","displayName":"IDC Storage and Hosting","parentId":188,"code":"NS","serialNum":"000","gitlabId":0},{"id":196,"name":"itinfrastructureproject","displayName":"IT Infrastructure Project","parentId":188,"code":"IP","serialNum":"000","gitlabId":0},{"id":198,"name":"jioitinfrastructure","displayName":"JIO IT Infrastructure","parentId":188,"code":"JI","serialNum":"000","gitlabId":0},{"id":200,"name":"wanprojects","displayName":"WAN Projects","parentId":188,"code":"WP","serialNum":"000","gitlabId":0},{"id":202,"name":"informationriskmanagement","displayName":"Information Risk Management","parentId":125,"code":"IR","serialNum":"001","gitlabId":0},{"id":204,"name":"applicationsecurity","displayName":"Application Security","parentId":202,"code":"AS","serialNum":"000","gitlabId":0},{"id":206,"name":"auditassurance","displayName":"Audit and Assurance","parentId":202,"code":"AA","serialNum":"000","gitlabId":0},{"id":208,"name":"compliancebenchmarking","displayName":"Compliance and Benchmarking","parentId":202,"code":"CB","serialNum":"000","gitlabId":0},{"id":210,"name":"datasecurity","displayName":"Data Security","parentId":202,"code":"DS","serialNum":"000","gitlabId":0},{"id":212,"name":"governancestrategy","displayName":"Governance and Strategy","parentId":202,"code":"GS","serialNum":"000","gitlabId":0},{"id":214,"name":"isoc","displayName":"ISOC","parentId":202,"code":"IS","serialNum":"000","gitlabId":0},{"id":216,"name":"riskarchitecture","displayName":"Risk and Architecture","parentId":202,"code":"RA","serialNum":"000","gitlabId":0},{"id":218,"name":"techsecsolutions","displayName":"Tech Sec Solutions","parentId":202,"code":"TS","serialNum":"000","gitlabId":0},{"id":220,"name":"marketingevents","displayName":"marketingevents","parentId":178,"code":"ME","serialNum":"000","gitlabId":0},{"id":222,"name":"fieldcrm","displayName":"Field & CRM","parentId":180,"code":"FC","serialNum":"000","gitlabId":0},{"id":224,"name":"saleschannel","displayName":"Sales & Channel","parentId":182,"code":"SC","serialNum":"000","gitlabId":0},{"id":226,"name":"businessplanningoptimization","displayName":"Business Planning & Optimization","parentId":184,"code":"BP","serialNum":"000","gitlabId":0},{"id":228,"name":"logistics","displayName":"Logistics","parentId":186,"code":"LO","serialNum":"000","gitlabId":0},{"id":230,"name":"treasury","displayName":"Treasury","parentId":154,"code":"TR","serialNum":"000","gitlabId":0},{"id":232,"name":"insurance","displayName":"Insurance","parentId":156,"code":"IN","serialNum":"000","gitlabId":0},{"id":234,"name":"directtaxes","displayName":"Direct Taxes","parentId":158,"code":"DT","serialNum":"000","gitlabId":0},{"id":236,"name":"indirecttaxes","displayName":"Indirect Taxes","parentId":160,"code":"ID","serialNum":"000","gitlabId":0},{"id":238,"name":"corporatesecretarial","displayName":"Corporate Secretarial","parentId":162,"code":"CS","serialNum":"000","gitlabId":0},{"id":240,"name":"consolidation","displayName":"Consolidation","parentId":164,"code":"CO","serialNum":"000","gitlabId":0},{"id":242,"name":"planningperformancemgmt","displayName":"Planning & Performance Mgmt.","parentId":166,"code":"PL","serialNum":"000","gitlabId":0},{"id":244,"name":"procuretopay","displayName":"Procure-to-Pay (Accounts Payable)","parentId":168,"code":"AP","serialNum":"000","gitlabId":0},{"id":246,"name":"ordertocash","displayName":"Order-to-Cash (Accounts Receivable)","parentId":170,"code":"AR","serialNum":"000","gitlabId":0},{"id":248,"name":"commissioningtoobsolescence","displayName":"Commissioning-to-Obsolescence(Asset Accounting)","parentId":172,"code":"AA","serialNum":"000","gitlabId":0},{"id":250,"name":"projectaccounting","displayName":"Project Accounting","parentId":174,"code":"PA","serialNum":"000","gitlabId":0},{"id":252,"name":"hiretoretire","displayName":"Hire-to-Retire (Payroll/ Benefits)","parentId":176,"code":"HR","serialNum":"000","gitlabId":0},{"id":254,"name":"categorymanagement","displayName":"Category Management","parentId":136,"code":"CM","serialNum":"000","gitlabId":0},{"id":256,"name":"intelligentesourcing","displayName":"Intelligent E-Sourcing","parentId":138,"code":"IE","serialNum":"000","gitlabId":0},{"id":258,"name":"fulfilmentmanagement","displayName":"Fulfilment Management","parentId":140,"code":"FM","serialNum":"000","gitlabId":0},{"id":260,"name":"logisticscontroltower","displayName":"Logistics Control Tower","parentId":142,"code":"LC","serialNum":"000","gitlabId":0},{"id":262,"name":"materialsmanagement","displayName":"Materials Management","parentId":144,"code":"MM","serialNum":"000","gitlabId":0},{"id":264,"name":"contractorlifecyclemanagement","displayName":"Contractor Lifecycle Management","parentId":146,"code":"CM","serialNum":"000","gitlabId":0},{"id":266,"name":"suppliersupport","displayName":"Supplier Support","parentId":148,"code":"SS","serialNum":"000","gitlabId":0},{"id":268,"name":"workingcapitalmanagement","displayName":"Working Capital Management","parentId":150,"code":"WM","serialNum":"000","gitlabId":0},{"id":270,"name":"servicesfcaplatform","displayName":"Services from FC&A platform","parentId":152,"code":"SF","serialNum":"000","gitlabId":0},{"id":272,"name":"salesdistribution","displayName":"Sales & Distribution","parentId":119,"code":"SD","serialNum":"000","gitlabId":0},{"id":274,"name":"lpg","displayName":"LPG","parentId":119,"code":"LP","serialNum":"000","gitlabId":0},{"id":276,"name":"industrial","displayName":"Industrial","parentId":119,"code":"IN","serialNum":"000","gitlabId":0},{"id":278,"name":"mops","displayName":"MOPS","parentId":117,"code":"MO","serialNum":"000","gitlabId":0},{"id":280,"name":"planning","displayName":"Planning","parentId":278,"code":"PL","serialNum":"000","gitlabId":0},{"id":282,"name":"scheduling","displayName":"Scheduling","parentId":278,"code":"SC","serialNum":"000","gitlabId":0},{"id":284,"name":"optimization","displayName":"Optimization","parentId":278,"code":"OP","serialNum":"000","gitlabId":0},{"id":286,"name":"trading","displayName":"Trading","parentId":117,"code":"TR","serialNum":"000","gitlabId":0},{"id":288,"name":"crudetrading","displayName":"Crude Trading","parentId":286,"code":"CT","serialNum":"000","gitlabId":0},{"id":290,"name":"gasprocurement","displayName":"Gas Procurement","parentId":286,"code":"GP","serialNum":"000","gitlabId":0},{"id":292,"name":"operationschartering","displayName":"Operations and Chartering","parentId":286,"code":"OC","serialNum":"000","gitlabId":0},{"id":294,"name":"producttrading","displayName":"Product Trading","parentId":286,"code":"PT","serialNum":"000","gitlabId":0},{"id":296,"name":"riskmanagament","displayName":"Risk Managament","parentId":286,"code":"RM","serialNum":"000","gitlabId":0},{"id":298,"name":"settlement","displayName":"Settlement","parentId":286,"code":"ST","serialNum":"000","gitlabId":0},{"id":300,"name":"enterprisecontentmanagement","displayName":"Enterprise Content Management","parentId":125,"code":"EC","serialNum":"000","gitlabId":0},{"id":302,"name":"dataservices","displayName":"Data Services","parentId":125,"code":"DS","serialNum":"000","gitlabId":0},{"id":304,"name":"enterprisecontentmanagement","displayName":"Enterprise Content Management","parentId":300,"code":"EC","serialNum":"000","gitlabId":0},{"id":306,"name":"dataengineering","displayName":"Data Engineering","parentId":302,"code":"DE","serialNum":"000","gitlabId":0},{"id":308,"name":"datamodeling","displayName":"Data Modeling","parentId":302,"code":"DM","serialNum":"000","gitlabId":0},{"id":310,"name":"datavisualization","displayName":"Data Visualization","parentId":302,"code":"DV","serialNum":"000","gitlabId":0},{"id":312,"name":"dataanalytics","displayName":"Data Analytics","parentId":302,"code":"DA","serialNum":"000","gitlabId":0}])

    #x=r.json()
    #x=json.loads(r)
    #df=pd.read_json(x)
    return r

def get_portfolios():
    df=get_portfolio_mapping()
    columns=['displayName','id']
    portfolios=df[df['parentId']==0][columns]
#    print(portfolios)
    return portfolios

def get_subportfolios(value):
    df=get_portfolio_mapping()
    columns=['displayName','id']
    subportfolios=df[df['parentId']== value][columns]
#    print('value =',value,'\n')
#    print(subportfolios)
    return subportfolios

def get_projects(one='',two=''):
    df= pd.DataFrame( [[row.project.key,row.project.name] for index,row in pd.DataFrame(jira_s.projects(), columns=['project']).iterrows()],columns=['project','projectname'])
    df=df[df['project'].str.contains(one+two)]
#    print(df)
    return df

def get_project_details(project):
    issues=pd.DataFrame(([issue.fields.project.name, issue.key, issue.fields.summary, issue.fields.status.name, issue.fields.issuetype.name] for issue in jira_s.search_issues("project ="+project)), columns=['Project Name','Issue ID','Issue Summary','Status','Issue Type'])
#    print(issues.columns)
    issue_type_count=pd.DataFrame(issues['Issue Type'].value_counts())
    issue_type_count['Story Type']=issue_type_count.index


#    print(issue_type_count)
    return issues,issue_type_count



def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    , className='table table-condensed col-sm-6')



layout = html.Div([
    html.H3('Project Dashboard'),
    dcc.Dropdown(
        id='portfolio_dd', className='col-sm-4',
        options=[
            {'label': row['displayName'], 'value': row['id'] } for index,row in get_portfolios().iterrows() 
        ]
    ),
    dcc.Dropdown(id='subportfolio_dd', className='col-sm-4'),
    dcc.Dropdown(id='project_dd', className='col-sm-4'),
    html.Div(id='project_table', className='col-sm-12'),
    html.Div(id='app-1-display-value')
    #,dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
        Output('subportfolio_dd', 'options'),
        [Input('portfolio_dd','value')])
def subportfolio_dd(value):
    options= [{'label':row['displayName'], 'value':row['id']} for index,row in get_subportfolios(value).iterrows()]
#    print(options)
    return options

@app.callback(
       # Output('project_table','children'),
       Output('project_dd','options'),
        [Input('portfolio_dd','value'),
        Input('subportfolio_dd','value')])
def project_dd(portfolio,subportfolio):
    df=get_portfolio_mapping()
    #project_list=get_projects('RM','')
    one = df[df['id']==portfolio]['code'].iloc[0] if portfolio else ''
    #if portfolio: print(one['code'].iloc[0])
    two = df[df['id']==subportfolio]['code'].iloc[0] if subportfolio else ''
    project_list = get_projects(one,two)
    return [{'label':project_list.iloc[i]['project']+' - '+project_list.iloc[i]['projectname'] , 'value':project_list.iloc[i]['project']} for i in range(len(project_list))]
 #   return generate_table(project_list,20)

@app.callback(
        Output('project_table','children'),
        [Input('project_dd','value')])
def project_table(project_id):
    issue_table=html.Div('No project Selected')
    test= html.Div('Please select project')
    if project_id:
        issues, issue_type_count = get_project_details(project_id)
        test= generate_table(issue_type_count,20)
        issue_table=generate_table(issues,20)

    return (test,issue_table)

