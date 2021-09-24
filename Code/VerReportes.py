from tkinter import *
from html2image import Html2Image
import webbrowser
class VerReportes():
    def __init__(self,recibo):    

        self.FrameReportes=Frame(recibo)
        labelframe = LabelFrame(self.FrameReportes, text="Tabla de Tokens",bg = "#1abc9c",bd=3,labelanchor='n',fg='white')
        labelframe.config(font=('Segoe UI', 12))
        labelframe2 = LabelFrame(self.FrameReportes, text="Tabla de Errores",bg = "#1abc9c",bd=3,labelanchor='n',fg='white')
        labelframe2.config(font=('Segoe UI', 12))
        #labelframe.grid()        
        #labelframe.grid(column=0, row=0, padx=20, pady=20)
      
        #Boton
        ButVerTokens=Button(labelframe,text ="Abrir Tabla de Tokens",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#0b5345',fg='white',command=self.generarTokens)
        ButVerTokens.pack(padx=20, pady=20)
        #Boton
        ButVerErrores=Button(labelframe2,text ="Abrir Tabla de Errores",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#0b5345',fg='white',command=self.generarErrores)
        ButVerErrores.pack(padx=20, pady=20)
 
       
        labelframe.pack(fill='y',padx=100, pady=50)
        labelframe2.pack(fill='y',padx=100, pady=50)
        self.FrameReportes.pack(fill='both', expand=True)
    
    def generarTokens(self):
        webbrowser.open_new_tab('file:///C:/Users/Usuario/Desktop/Lenguajes/LFP_Proyecto1_201903791/Code/Tabla%20de%20Tokens/index.html')
        

    def generarErrores(self):
        rt='file:///C:/Users/Usuario/Desktop/Lenguajes/LFP_Proyecto1_201903791/Code/Tabla%20de%20Errores/index.html'
        webbrowser.open_new_tab(rt)

