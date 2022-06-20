from cargarTipoCambio import  grabarMonedas,lista_tipocambio

def exportarTipoCambio():

   strMonedas = grabarMonedas(lista_tipocambio())
   fw = open('monedas.csv','w')
   fw.write(strMonedas)
   fw.close()

   return strMonedas