from bs4 import BeautifulSoup
import requests
import pandas as pd
#pd.options.display.max_columns = None
import datetime
from tabulate import tabulate
from pytz import timezone


class Complex:
    
    def __init__(self, zonales):
        self.d = zonales

        def esc(code):
            return f'\033[{code}m'
          
        # using now() to get current time 
        current_time = datetime.datetime.now(timezone('America/Bogota')) 

        dia = current_time.strftime("%d")
        mes = current_time.strftime("%m")
        anio = current_time.strftime("%Y")


        ##########
        #VARIABLES#

        fecha = anio+'-'+mes+'-'+dia

        print('FECHA DE CONSULTA: ',fecha,"\n################")



        consulta = "declare @cataa int,@catai int, @promotion int, @promotiond int, @promotiondp int, @generico int, @cpa int, @pa int \
        select top 100 @cataa=(select count(*) from Catalog where catActive='1') \
        select @catai=(select count(*) from Catalog where _deleted='1') \
        select @promotion=(select count(*) from promotion) \
        select @promotiond=(select count(*) from promotiondetail) \
        select @promotiondp=(select count(*) from promotiondetailproduct) \
        select @generico=(select count(*) from customerstatus where cusCode like'%099999999%') \
        select @cpa=(select count(*) from customerpartner) \
        select @pa=(select count(*) from partner) \
        select @cataa as CA, @catai as CI, @promotion as PROMOTION, @promotiond as PROMOTIOND, @promotiondp as PROMOTIONDP, @generico as GENERICO, @cpa CUSPAR, @pa PAR"


        consulta2 = "declare @customerxss int, @cusdelete int, @customerroute int, @cusst int, @customerstatus int, @customerroute1 int, @product int, @catalog int \
        select @customerxss= (select top 100 count(*) from customer) \
        select @cusdelete=(select count(*) from customer where _Deleted='0' ) \
        select @customerroute=(select count(distinct cuscode) from customerroute where ctrvisittoday='1' and rotcode not like'%t%') \
        select @customerstatus=(select count(*) from customerstatus WHERE CUSCODE IN (SELECT CUSCODE FROM CUSTOMERROUTE)) \
        select @cusst=(select count(*) from customerstatus where cuscode in(select cusCode from customerroute where ctrVisitToday='1' and rotcode not like'%t%')) \
        select @customerroute1=(select count(distinct cuscode) from customerroute) \
        select @product=(select count(*) from product where _Deleted='0') \
        select @catalog=(select count(*) from CatalogDetail where catCode like'%NacDZ%')\
        select @customerxss as CUST_XSS, @cusdelete as CUST_DELETE_0, @customerroute1 as CUSROUT_TOTAL,@customerroute as CUSROUTE_VISIT_TODAY,@cusst as CUSSTATUS_VISIT_TODAY, @customerstatus as CUSSTATUS_TOTAL, @product as PRODUCT, @catalog as CATALOGO"




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

        def logear_sesion(cc,zonal,p):
            
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
              'password': p
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

        def ejecutar_consulta(cc,ee,zonal,q):

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

            
            data = {
              '__EVENTTARGET': '',
              '__EVENTARGUMENT': '',
              '__LASTFOCUS': '',
              '__VIEWSTATE': '',
              'Ddl_BaseDatos': ''+zonal+'_XSS_441_PRD',
              'optradio': 'Rb_DecimalCo',
              'TxtSql': q,
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
            print("---------------------------------------------------")
            print("---------------------------------------------------")
            #print(zonal, " : " ,opciones[0]['value'])
            print(esc('45'),zonal, " : " ,opciones[0]['value'],esc('0'))
            if len(fragmentList)>0:
                df_list = pd.read_html(response.text) # this parses all the tables in webpages to a list
                df = df_list[0]
                #df.head()
                print(tabulate(df, headers='keys', tablefmt='psql'))
            else:
                print("No hay informacion")

        def principal(zonal,q,p):
            cc = obtener_sesion(zonal)
            logear_sesion(cc,zonal,p)
            ee = obtener_event(cc,zonal)
            ejecutar_consulta(cc,ee,zonal,q)
            
        for clave,valor in zonales.items():
            principal(clave,consulta,valor)
            principal(clave,consulta2,valor)

