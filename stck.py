from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import pandas as pd
#pd.options.display.max_columns = None



zonales = ['PRONACA']
almacenes = ['D01','D02','D03','D04','D05']



#################################
### OBTENEMOS SESION Y COOKIES###

def obtener_sesion(zonal):    
    session = requests.Session()
    payload = {'connectionName':''+zonal+'_XSS_441_PRD'}
    s = session.get("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/Index")
    cc = s.cookies['ASP.NET_SessionId']
    s = session.post("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/validatedSession")
    s = session.post("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/serverVersion")
    s = session.post("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/DisplayDDListConnections")
    s = session.post("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/setConnection", data=payload)
    s = session.post("https://prd1.xsalesmobile.net/"+zonal+"/xsm/Login/SetLanguage")

    return cc

#########################
### LOGEAMOS LA SESION###

def logear_sesion(cc,zonal):
    
    cookies = {
        'ASP.NET_SessionId': cc,
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Referer': 'https://prd1.xsalesmobile.net/'+zonal+'/xsm/Login/Index',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '0',
        'Origin': 'https://prd1.xsalesmobile.net',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = {
      'connectionName': ''+zonal+'_XSS_441_PRD',
      'username': 'Soporte.nuo',
      'password': 'Nuo2021*'
    }

    response = requests.post('https://prd1.xsalesmobile.net/'+zonal+'/xsm/Login/userLogonServer', headers=headers, cookies=cookies, data=data)


######################
### OBTENEMOS EVENT###

def obtener_event(cc,zonal):

    cookies = {
        'ASP.NET_SessionId': cc,
    }

    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://prd1.xsalesmobile.net/'+zonal+'/xsm/app/css/global.css?vcss=20191107',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Origin': 'https://prd1.xsalesmobile.net',
    }

    response = requests.get('https://prd1.xsalesmobile.net/'+zonal+'/xsm/app/webForms/webTools/sqlQuery/DBQueryUI.aspx', headers=headers, cookies=cookies)

    html_brute = response.text
    soup = BeautifulSoup(html_brute, "html.parser")

    fragmentList = soup.findAll("input")
    ff = soup.find("input", {"id": "__EVENTVALIDATION"})
    ee= ff.get('value')

    return ee


#############################
### EJECUTAMOS LA CONSULTA###

def ejecutar_consulta(cc,ee,zonal,almacen):

    cookies = {
        'ASP.NET_SessionId': cc,
    }    

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://prd1.xsalesmobile.net',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.197',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://prd1.xsalesmobile.net/'+zonal+'/xsm/app/css/global.css?vcss=20191107',
        'Accept-Language': 'es-ES,es;q=0.9',
    }

    query = "declare @preventa datetime, @despacho date, @horainicio datetime, @horafin datetime \
    select @preventa= (select  top(1) exvDateValue from dbo.extendedTableValue3 where exfFieldName='x_aptTransactionDate' and exvPKCode1='"+almacen+"') \
    select @despacho= (select  top(1) exvDateValue from dbo.extendedTableValue3 where exfFieldName='x_aptServerLastUpdate' and exvPKCode1='"+almacen+"') \
    select @horainicio=(SELECT max(Trndate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and trnScripts like'%"+almacen+"%') \
    select  @horafin=(SELECT max(trnLastDate) FROM[TRANSACTION] WHERE TRNSCRIPTS LIKE'%CALCULATE%' and trnScripts like'%"+almacen+"%') \
    select @preventa as PREVENTA, @despacho as DESPACHO, dateadd(hh,-1,@horainicio) as HORA_ENVIO_EC,dateadd(hh,-1,@horafin) as HORA_FIN_EC"
    data = {
      '__EVENTTARGET': '',
      '__EVENTARGUMENT': '',
      '__LASTFOCUS': '',
      '__VIEWSTATE': '',
      'Ddl_BaseDatos': ''+zonal+'_XSS_441_PRD',
      'optradio': 'Rb_DecimalCo',
      'TxtSql': query,
      'lblBtnExecute': 'Ejecutar',
      'ddlExport': '-1',
      '__SCROLLPOSITIONX': '0',
      '__SCROLLPOSITIONY': '0',
      '__EVENTVALIDATION': ee
    }

    response = requests.post('https://prd1.xsalesmobile.net/'+zonal+'/xsm/app/webForms/webTools/sqlQuery/DBQueryUI.aspx', headers=headers, cookies=cookies, data=data)


    html_brute = response.text
    soup = BeautifulSoup(html_brute, "html.parser")
    fragmentList = soup.findAll("table")
    opciones = soup.findAll("option")
    print("STOCK ALMACEN:", almacen, ' : ', zonal, " : " ,opciones[0]['value'])
    if len(fragmentList)>0:
        df_list = pd.read_html(response.text) # this parses all the tables in webpages to a list
        df = df_list[0]
        #df.head()
        #df.to_csv('a.csv', index=False)
        #df.to_excel (r'export_dataframe.xlsx', index = False, header=True, sheet_name=zonal)
        #print(df_list)
        print(tabulate(df, headers='keys', tablefmt='psql'))
    else:
        print("No hay informacion")
    

    

def principal(zonal):
    cc = obtener_sesion(zonal)
    logear_sesion(cc,zonal)
    ee = obtener_event(cc,zonal)
    for almacen in almacenes:
        ejecutar_consulta(cc,ee,zonal,almacen)


print("INFORME STOCK \n#################")
for zonal in zonales:
        principal(zonal)

  


