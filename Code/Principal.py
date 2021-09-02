from tkinter import *

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title('Bitxelart')
        self.root.geometry('500x500')
    

    def create_widgets(self):
        self.hi_there=Button(self.root,text="Hello World\n(click me)", fg="blue",command=self.say_hi)  
        self.quit=Button(self.root,text="QUIT", fg="red",command=self.root.destroy)

        self.hi_there.pack(side="top")
   
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


Aps=Application()
Aps.create_widgets()
Aps.root.mainloop()