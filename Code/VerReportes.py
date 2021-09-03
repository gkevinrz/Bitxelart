from tkinter import *

class VerReportes():
    def __init__(self,recibo):    

        self.frameprueba=Frame(recibo)
        self.label= Label(self.frameprueba,text='Prueba')
        self.label.pack()
        
        self.web_button = Button(self.frameprueba, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = Button(self.frameprueba, text="Visitar foro")
        self.forum_button.pack(side=LEFT)