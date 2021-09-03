from tkinter import *
from tkinter import ttk
from AnalizarArchivo import AnalizarArchivo
from VerReportes import VerReportes
class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title('Bitxelart')
        self.root.geometry('800x800')
        self.root.iconbitmap('Images/Icono.ico')
        self.root.config(bg='#2E4053')
    def create_widgets(self):
        
        #self.hi_there=Button(self.root,text="Hello World\n(click me)", fg="blue",command=self.say_hi)  
        #self.quit=Button(self.root,text="QUIT", fg="red",command=self.root.destroy)
        #self.hi_there.pack(side="top")
        #self.quit.pack(side="bottom")
        #
        panelprueba=ttk.Notebook(self.root)
        p=AnalizarArchivo(panelprueba)
        p2=VerReportes(panelprueba)
        panelprueba.add(p.frameprueba,text="AnalizarArchivo", padding=10)
        panelprueba.add(p2.frameprueba,text="Ver Reportes", padding=10)

        panelprueba.pack(pady=10, expand=True)
        


    def say_hi(self):
        print("hi there, everyone!")


Aps=Application()
Aps.create_widgets()
Aps.root.mainloop()