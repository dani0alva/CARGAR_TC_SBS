import tkinter
from tkinter import  *
from tkinter.ttk import Treeview
from cargarTipoCambio import  lista_tipocambio
from exportarTipoCambio import  exportarTipoCambio
from tkinter import messagebox
class TipoCambio:

    def __init__(self,window):
        self.wind = window
        self.wind.title('TIPO DE CAMBIO SBS')
        self.wind.geometry('670x390')
        self.wind.configure(bg='#49A')

        #frame
        frame = LabelFrame(self.wind,text='Exportar tipo de Cambio SBS')
        frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)

        
        #BOTON DescargarTC
        btncargarGrig = Button(frame,text='DescargarTC',command=self.descargarTC)
        btncargarGrig.grid(row=4,column=1,columnspan=1,sticky=W+E)
       

        #BOTON exportarGrid
        btnexportarTC = Button(frame,text='CargarGrid',command=self.cargarTC)
        btnexportarTC.grid(row=4,column=2,columnspan=1,sticky=W+E)
        
        #TREVIEW
        self.TrvTipoCambio = Treeview(frame, height=10, columns=("#1","#2"), selectmode="extended")
        self.TrvTipoCambio.grid(row=5,column=0,columnspan=4,padx=10)
        self.TrvTipoCambio.heading('#0',text='Moneda',anchor=CENTER)
        self.TrvTipoCambio.heading('#1',text='Compra',anchor=CENTER)
        self.TrvTipoCambio.heading('#2',text='Venta',anchor=CENTER)

    ListaTC = []

    def cargarTC(self):
        ListaTC=lista_tipocambio()
        
        strMonedas = ""
        for listDic in ListaTC:
            item=self.TrvTipoCambio.insert('',0,text=listDic['moneda'],values=[listDic['compra'],listDic['venta']])

    def descargarTC(self):
        exportarTipoCambio()
        messagebox.showinfo("Se descargo con exito un archivo csv ")

window = Tk()
app = TipoCambio(window)
window.mainloop()