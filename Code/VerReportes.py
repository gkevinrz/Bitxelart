from tkinter import *
from html2image import Html2Image

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
        ButVerTokens=Button(labelframe,text ="Generar tabla de tokens",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#0b5345',fg='white',command=self.generarTokens)
        ButVerTokens.pack(padx=20, pady=20)
        #Boton
        ButVerErrores=Button(labelframe2,text ="Generar tabla de errores",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#0b5345',fg='white',command=self.generarErrores)
        ButVerErrores.pack(padx=20, pady=20)
 
       
        labelframe.pack(fill='y',padx=100, pady=50)
        labelframe2.pack(fill='y',padx=100, pady=50)
        self.FrameReportes.pack(fill='both', expand=True)
    
    def generarTokens(self):
        pass

    def generarErrores(self):
        pass
    #def say_hi(self):
     #   hti = Html2Image()
      #  hti.screenshot(html_file='Prueba.html', css_file='css_prueba.css',save_as='blue_page.png',size=(200,200))