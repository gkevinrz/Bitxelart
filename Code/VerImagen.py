from tkinter import *
from html2image import Html2Image
class VerImagen():
    def __init__(self,recibo,Titulos):
        self.listaTitulos=Titulos
        self.FrameVerImagen=Frame(recibo)
        labelframe = LabelFrame(self.FrameVerImagen, text="Seleccione una imagen",bg = "#1b4f72",bd=3,labelanchor='n',fg='white')
        labelframe.config(font=('Segoe UI', 12))

        ButAbrirArchivo=Button(labelframe,text ="Abrir archivo",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#17202a',fg='white',command=self.hola)
        ButAbrirArchivo.pack(padx=20, pady=20)

        labelframe.pack(fill='x',padx=100, pady=50)
        self.FrameVerImagen.pack(fill='both', expand=True)
    def hola(self):
        print(self.listaTitulos)
       