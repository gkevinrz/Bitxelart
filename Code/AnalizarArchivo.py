from tkinter import *
class AnalizarArchivo():
    
    def __init__(self,recibo):    

        self.frameprueba=Frame(recibo)
        self.label= Label(self.frameprueba,text='Visitanos en recursospython.com y foro.recursospython.com')
        self.label.pack()
        
        self.web_button = Button(self.frameprueba, text="Visitar web")
        self.web_button.pack(pady=10)
        
        self.forum_button = Button(self.frameprueba, text="Visitar foro")
        self.forum_button.pack(side=LEFT)
       