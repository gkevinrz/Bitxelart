from tkinter import *
class VerImagen():
    def __init__(self,recibo):

        self.FrameVerImagen=Frame(recibo)
        labelframeCombo = LabelFrame(self.FrameVerImagen, text="Seleccione una imagen")
        labelframeCombo.pack(side=RIGHT)
     
        self.FrameVerImagen.pack()
       