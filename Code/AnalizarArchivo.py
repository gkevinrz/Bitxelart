from tkinter import *
class AnalizarArchivo():
    
    def __init__(self,recibo):
        self.FrameAnalizar=Frame(recibo)
        labelframe = LabelFrame(self.FrameAnalizar, text="This is a LabelFrame")
        #labelframe.grid()        
        labelframe.grid(column=0, row=0, padx=20, pady=20)
        labelframe.pack(fill='both',expand=True,padx=20, pady=20)
        self.FrameAnalizar.pack(fill='both', expand=True)
       