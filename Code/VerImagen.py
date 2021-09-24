from tkinter import *
from tkinter import ttk
import tkinter
from html2image import Html2Image
from functools import partial
from tkinter import messagebox
from PIL import ImageTk,Image  
import os
ListaTitulos=[]


class VerImagen():
    def __init__(self,recibo):

        self.listaTitulos=ListaTitulos
        self.FrameVerImagen=Frame(recibo)
        self.imagen=None
        self.imagenOriginal=None
        self.imagenMirrorX=None 
        self.imagenMirrorY=None
        self.imagenDoubleMirror=None

        labelframe = LabelFrame(self.FrameVerImagen, text="Seleccione una imagen",bg = "#5499c7",bd=3,labelanchor='n',fg='white')
        labelframe.config(font=('Segoe UI', 12))
        
        labelFrame2=LabelFrame(self.FrameVerImagen,text='Filtros',bg="#2c3e50",bd=3,labelanchor='n',fg="white",font=('Segoe UI', 12),height=200)
        #labelFrame2.grid_propagate(0
        #labelFrame2.grid(column=1,row=4,columnspan=2, sticky="E",padx=5, pady=0, ipadx=0, ipady=0)
        labelFrame2.place(x=40, y=134,width=200,height=400)
        
        self.ButtonVerImagenes=Button(labelframe,text='Ver Imagenes',font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#eaeded',fg='black',command=self.llenarCombo)
        self.ButtonVerImagenes.place(x=20, y=10,width=100,height=30)

        self.BMirrox=Button(labelFrame2,text ="Mirror X",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#FFFFFF',fg='black')
        self.BMirrox.pack(padx=20, pady=20)
        
        self.BMirroY=Button(labelFrame2,text ="Mirror Y",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#FFFFFF',fg='black')
        self.BMirroY.pack(padx=20, pady=40)

        self.dBMirror=Button(labelFrame2,text ="Double Mirror",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#FFFFFF',fg='black')
        self.dBMirror.pack(padx=20, pady=20)
        self.combo=ttk.Combobox(labelframe,state="readonly")
        

        self.combo.bind('<<ComboboxSelected>>',self.NombreImagen)
        self.combo.pack(padx=10, pady=10)
        labelframe.place(x=40, y=20,width=400,height=90)
        #load = Image.open('Super Mario Bros 64/DoubleMirror.png')
        #self.imagen = ImageTk.PhotoImage(load) # aquí
        #label = Label(self.FrameVerImagen, image=self.imagen) # aquí
        #label.place(x=400, y=-100,width=700,height=800)
        #canvas = Canvas(self.FrameVerImagen)     
        #canvas.place(x=300, y=150,width = 300, height = 300)
        #img = ImageTk.PhotoImage(Image.open('Images/pixel-art.jpg'))     
        #canvas.create_image(20,20, anchor=N, image=img)   
        self.FrameVerImagen.pack(fill='both', expand=True)
    
    def llenarCombo(self):
        self.combo['values']=self.listaTitulos

    def NombreImagen(self,event):
        self.verMirrorX(self.combo.get())
        self.verMirrorY(self.combo.get())
        self.verDBMirror(self.combo.get())
        self.original(self.combo.get())

    def original(self,nombre):
        load = Image.open(f'{nombre}/Original.png')
        self.imagenOriginal = ImageTk.PhotoImage(load) # aquí
        label = Label(self.FrameVerImagen, image=self.imagenOriginal) # aquí
        label.place(x=400, y=-100,width=700,height=800)


    def verMirrorX(self,nombre):
        self.BMirrox.config(command=partial(self.makeMirrorX,nombre))

    def makeMirrorX(self,nombreArchivo):
        if self.existeMirrorx(nombreArchivo):
            load = Image.open(f'{nombreArchivo}/MirrorX.png')
            self.imagenMirrorX = ImageTk.PhotoImage(load) # aquí
            label = Label(self.FrameVerImagen, image=self.imagenMirrorX) # aquí
            label.place(x=400, y=-100,width=700,height=800)
        else:
            messagebox.showerror(title='Error', message='No se encontró el archivo')

    def existeMirrorx(self,filePath):
        try:
            with open(f'{filePath}/MirrorX.png', 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False



    def verMirrorY(self,nombre):
        self.BMirroY.config(command=partial(self.makeMirrorY,nombre))
        #print(nombre)

    def makeMirrorY(self,nombreArchivo):
        if self.existeMirrorY(nombreArchivo):
            load = Image.open(f'{nombreArchivo}/MirrorY.png')
            self.imagenMirrorY = ImageTk.PhotoImage(load) # aquí
            label = Label(self.FrameVerImagen, image=self.imagenMirrorY) # aquí
            label.place(x=400, y=-100,width=700,height=800)   
        else:
            messagebox.showerror(title='Error', message='No se encontró el archivo')


    def existeMirrorY(self,filepath):
        try:
            with open(f'{filepath}/MirrorY.png', 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False


    def verDBMirror(self,nombre):
        self.dBMirror.config(command=partial(self.makeDBMirror,nombre))


    def makeDBMirror(self,nombrearchivo):
        if self.existeDBmirror(nombrearchivo):
            load = Image.open(f'{nombrearchivo}/DoubleMirror.png')
            self.imagenDoubleMirror = ImageTk.PhotoImage(load) # aquí
            label = Label(self.FrameVerImagen, image=self.imagenDoubleMirror) # aquí
            label.place(x=400, y=-100,width=700,height=800)   
        else:
            messagebox.showerror(title='Error', message='No se encontró el archivo')

    def existeDBmirror(self,filepath):
        try:
            with open(f'{filepath}/DoubleMirror.png', 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False
      