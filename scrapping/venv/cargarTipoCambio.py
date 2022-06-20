import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx")

def grabarMonedas(monedas):
    """
    convierte una lista de diccionarios en una cada string
    """
    strMonedas = ""
    for l in monedas:
        for clave,valor in l.items():
            strMonedas += valor
            if clave != 'venta':
                strMonedas += ';'
            else:
                strMonedas += '\n'
    return strMonedas


def lista_tipocambio():

    if(url.status_code == 200):
        print("pagina encontrada")
        #print(url.text)
        html = BeautifulSoup(url.text,'html.parser')
        tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
        #print(tabla)
        #filaDolar = html.find_all('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__0'})
        #print(filaDolar)
     
        listaMonedas = []
        for i in range(7):
            fila = html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)}) 
            moneda = fila.find('td',{'class':'APLI_fila3'})
            compra = fila.find('td',{'class':'APLI_fila2'})
            venta = fila.find('td',{'class':'APLI_fila2'}).findNext('td')
            dicMoneda = {
                'moneda': moneda.get_text(),
                'compra': compra.get_text(),
                'venta': venta.get_text()
            }
            listaMonedas.append(dicMoneda)
        
      
    else:
        print("error " + str(url.status_code))

    return listaMonedas
    