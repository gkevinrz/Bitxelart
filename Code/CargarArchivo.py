
from os import error, linesep,mkdir
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Error import Error
from Token import Token

ListaTituloGlobal=[]
class CargarArchivo():
    
    def __init__(self,recibo):
        self.PalabrasReservadas=['TITULO','CELDAS','FILTROS','ALTO','ANCHO','FILAS','COLUMNAS']
        self.Simbolos=['=','"',';','{','[','#',']','}','@']
        self.ListaErrores=[]
        self.ListaTokens=[]
        self.TextoEntrada=''
        ######################
        self.Titulos=[]
        self.Anchos=[]
        self.Altos=[]
        self.Filas=[]
        self.Columnas=[]
        self.Filtros=[]
        self.FiltrosAux=[]
        self.Colores=[]
        self.ColoresAux=[]
        self.Booleans=[]
        self.BooleansAux=[]
        self.Posiciones=[]
        self.PosicionesTotales=[]
        self.PosicionesAux=[]
        self.PosicionesAux2=[]
        ##########################
        self.FrameCargar=Frame(recibo)
        labelframe = LabelFrame(self.FrameCargar, text="Seleccione un archivo de entrada .pxla",bg = "#1b4f72",bd=3,labelanchor='n',fg='white')
        labelframe.config(font=('Segoe UI', 12))
        labelframe2 = LabelFrame(self.FrameCargar, text="Analizar Archivo",bg = "#1b4f72",bd=3,labelanchor='n',fg='white')
        labelframe2.config(font=('Segoe UI', 12))
        #labelframe.grid()        
        #labelframe.grid(column=0, row=0, padx=20, pady=20)
      
        #Boton
        ButAbrirArchivo=Button(labelframe,text ="Abrir archivo",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#17202a',fg='white',command=self.select_file)
        ButAbrirArchivo.pack(padx=20, pady=20)
        #Boton
        ButAnalizarArchivo=Button(labelframe2,text ="Analizar archivo",font=('Segoe UI', 12),bd=0,pady=10,padx=10,bg='#17202a',fg='white',command=self.Lectura)
        ButAnalizarArchivo.pack(padx=20, pady=20)
 
       
        labelframe.pack(fill='x',padx=100, pady=50)
        labelframe2.pack(fill='x',padx=100, pady=50)
        self.FrameCargar.pack(fill='both', expand=True)
        
        

    def select_file(self):
        filetypes = (('Archivos pxla', '*.pxla'),('Todos los archivos', '*.*'))
        archivo = filedialog.askopenfile(title='Abrir un archivo',initialdir='./',filetypes=filetypes)
        if archivo is None:
            messagebox.showerror(title='Error', message='No se eligió ningún archivo')
            return None
        else:
            texto = archivo.read()
            archivo.close()
            messagebox.showinfo(title='Información', message='Archivo cargado exitosamente')
            #print(texto)
            self.TextoEntrada=texto

    def Lectura(self):
        if self.TextoEntrada is not None:
            #print(textoanalizar)
            self.TextoEntrada+= "~"
            messagebox.showinfo(title='Información', message='Lectura exitosa')
            self.Analizar(self.TextoEntrada)
            #print(self.TextoEntrada)
        else:
            messagebox.showerror(title='Error', message='No se pudo analizar la entrada, intenta de nuevo')
        
    #Letra
    def isLetra(self,caracter):
        if((ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122) or ord(caracter) == 164 or ord(caracter) == 165):
            return True
        else:
    #Numero
            return False 
    def isNumero(self,caracter):
        if ((ord(caracter) >= 48 and ord(caracter) <= 57)):
            return True
        else:
            return False
            #="";{}[],@
    def isSimbolo(self,caracter):
        if (ord(caracter)==35 or ord(caracter)==34 or ord(caracter)==44 or ord(caracter)==59 or ord(caracter)==61 or ord(caracter)==64 or ord(caracter)==91 or ord(caracter)==93 or ord(caracter)==123 or ord(caracter)==125 or ord(caracter)==126):
            return True
        else:
            return False
    def isHxdecimal(self,caracter):
        if ((ord(caracter) >= 65 and ord(caracter) <= 70) or (ord(caracter)>=97 and ord(caracter)<=102) or (ord(caracter)>=48 and ord(caracter)<=57)):
            return True
        else:
            return False
    
    def Analizar(self,text):
        error=False
        fila = 1
        columna = 0
        estado = 0
        lexActual = ""
        #cont=0
        for c1 in text:
            if self.isLetra(c1) or self.isNumero(c1) or self.isSimbolo(c1):
                columna+=1
                continue
            elif (ord(c1) == 10):
                columna = 0
                fila += 1
                continue
            elif (ord(c1) == 9):
                columna += 4
                continue
            elif (ord(c1) == 32):
                columna += 1
                continue
            else:
                columna+=1
                err=Error('Lexico',fila,columna,'Caracter Invalido. Corregir archivo',c1)
                self.ListaErrores.append(err)
                error=True
                continue
    
        for ob in self.ListaErrores:
            print(ob.tipoError,ob.descripcion,ob.filaError,ob.columnaError,ob.caracter)
        if error==True:
            messagebox.showerror(title='Error', message='Caracteres Inválidos, por favor corregir. Ver tabla de errores')
            
        else:
            fila=1
            columna=0
            contT=0
            tokenPalabraR=''
            tokencadena=''
            tokenNumero=''
            tokenFiltro=''
            tokenColor=''
            tokenBoolean=''
            tokenX=''
            tokenY=''
            vAlto=None
            vAncho=None

            for c in text:    
                if estado==0:
                    #CON T
                    if self.isLetra(c) and ord(c)==84:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=1
                    #CON A
                    elif self.isLetra(c) and ord(c)==65:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=12
                    #CON F
                    elif self.isLetra(c) and ord(c)==70:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=20
                        
                    #CON C
                    elif self.isLetra(c) and ord(c)==67:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=34
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)==64:
                            pass
                        elif self.isNumero(c):
                            err=Error('Sintactico',fila,columna,'Se esperaba una T o C o F o A',c)
                            self.ListaErrores.append(err)
                elif estado==1:
                    if self.isLetra(c) and ord(c)==73:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=2
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=73:
                            err=Error('Sintactico',fila,columna,'Se esperaba una I',c)
                            self.ListaErrores.append(err)
                    #else: #@
                     #   err=Error('Lexico',fila,columna - (len(lexActual) - 1),'Caracter Inválido',c)
                      #  self.ListaErrores.append(err)
                elif estado==2:
                    if self.isLetra(c) and ord(c)==84:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=3
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or ord(c)!=84:
                            err=Error('Sintactico',fila,columna,'Se esperaba una T',c)
                            self.ListaErrores.append(err)
                elif estado==3:
                    if self.isLetra(c) and ord(c)==85:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c                     
                        estado=4
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or ord(c)!=85:
                            err=Error('Sintactico',fila,columna,'Se esperaba una U',c)
                            self.ListaErrores.append(err)
                elif estado==4:
                    if self.isLetra(c) and ord(c)==76:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c                      
                        estado=5
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or ord(c)!=76:
                            err=Error('Sintactico',fila,columna,'Se esperaba una L',c)
                            self.ListaErrores.append(err)
                elif estado==5:
                    if self.isLetra(c) and ord(c)==79:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=6      
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or ord(c)!=79:
                            err=Error('Sintactico',fila,columna,'Se esperaba una O',c)
                            self.ListaErrores.append(err)
                elif estado==6:
                    contT+=1
                    token=Token(contT,tokenPalabraR,fila,columna-(len(tokencadena)-1),'Palabra Reservada')
                    self.ListaTokens.append(token)
                    #tokenPalabraR=''       
                    if ord(c)==61:
                        lexActual=lexActual+c
                        estado=7
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=61:
                            err=Error('Sintactico',fila,columna,'Se esperaba =',c)
                            self.ListaErrores.append(err)           
                elif estado==7:
                    if ord(c)==34:
                        lexActual=lexActual+c
                        estado=8
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=34:
                            err=Error('Sintactico',fila,columna,'Se esperaba " ',c)
                            self.ListaErrores.append(err)
                elif estado==8:

                    #if self.isLetra(c):
                    lexActual=lexActual+c
                    tokencadena=tokencadena+c
                    estado=9                       
                    #else:
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    #else:
                            #err=Error('Sintactico',fila,columna,'Se esperaba texto',c)
                            #self.ListaErrores.append(err)        
                elif estado==9:
                    #if #self.#isLetra(c):
                    if ord(c)!=34:
                        lexActual=lexActual+c
                        tokencadena=tokencadena+c
                        estado=9    
                        #self.Titulos.append(lexActual)
                    if ord(c)==34:
                        lexActual=lexActual+c
                        estado=10
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        #elif ord(c)!=34:
                            #err=Error('Sintactico',fila,columna,'Se esperaba una cadena o "',c)
                            #self.ListaErrores.append(err)                  
                elif estado==10:
                    #print(columna)
                    contT+=1
                    token=Token(contT,tokencadena,fila,columna-(len(tokencadena)),'Cadena')
                    self.ListaTokens.append(token)
                    self.Titulos.append(tokencadena)
                    if ord(c)==59:
                        lexActual=lexActual+c
                        estado=11
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif  ord(c)!=59:
                            err=Error('Sintactico',fila,columna,'Se esperaba ; ',c)
                            self.ListaErrores.append(err) 
                elif estado==11:
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                        #err=Error('Sintactico',fila,columna - (len(lexActual) - 1),'Se espera ANCHO o ALTO o FILAS o COLUMNAS o CELDA o FILTROS',c)
                        #self.ListaErrores.append(err)
                    lexActual=''
                    tokenPalabraR=''
                    tokencadena=''
                    estado=0
                ###################AQUI EMPIEZA ANCHO O ALTO##########################
                elif estado==12:
                    if self.isLetra(c) and ord(c)==78:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=13
                    elif self.isLetra(c) and ord(c)==76:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=13
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=78 or ord(c)!=76:
                            err=Error('Sintactico',fila,columna,'Se esperaba una N o L',c)
                            self.ListaErrores.append(err)
                elif estado==13:
                    if self.isLetra(c) and ord(c)==67:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=14
                    elif self.isLetra(c) and ord(c)==84:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=14
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=67 or ord(c)!=84:
                            err=Error('Sintactico',fila,columna,'Se esperaba una C o T',c)
                            self.ListaErrores.append(err)
                elif estado==14:
                    if self.isLetra(c) and ord(c)==79:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=15
                    elif self.isLetra(c) and ord(c)==72:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=15
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=79 or ord(c)!=72:
                            err=Error('Sintactico',fila,columna,'Se esperaba una H o O',c)
                            self.ListaErrores.append(err)
                elif estado==15:
                    if self.isLetra(c) and ord(c)==79:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=16
                    elif ord(c)==61:
                        lexActual=lexActual+c
                        vAlto=True
                        #vAncho=False
                        estado=17
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=79 or ord(c)!=61:
                            err=Error('Sintactico',fila,columna,'Se esperaba una O o =',c)
                            self.ListaErrores.append(err)
                elif estado==16:
                    if ord(c)==61:
                        lexActual=lexActual+c
                        vAncho=True
                        estado=17
                        #vAlto=False
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=61:
                            err=Error('Sintactico',fila,columna,'Se esperaba una O o =',c)
                            self.ListaErrores.append(err)
                elif estado==17:
                    contT+=1
                    token=Token(contT,tokenPalabraR,fila,columna-(len(tokenPalabraR)),'Palabra Reservada')
                    self.ListaTokens.append(token)
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=18
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c)==False:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito',c)
                            self.ListaErrores.append(err)
                elif estado==18:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=18
                    elif ord(c)==59:
                        if vAncho==True:
                            contT+=1
                            token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                            self.ListaTokens.append(token)
                            self.Anchos.append(int(tokenNumero))
                        elif vAlto==True:
                            contT+=1
                            token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                            self.ListaTokens.append(token)
                            self.Altos.append(int(tokenNumero))
                        lexActual=lexActual+c
                        estado=19 
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o ;',c)
                            self.ListaErrores.append(err)
                elif estado==19:
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                        #err=Error('Sintactico',fila,columna - (len(lexActual) - 1),'Se espera ANCHO o ALTO o FILAS o COLUMNAS o CELDA o FILTROS',c)
                        #self.ListaErrores.append(err)
                    lexActual=''
                    tokenPalabraR=''
                    tokenNumero=''
                    vAncho=None
                    vAlto=None
                    estado=0
                #############AQUI EMPIeZA FILTROS Y FILAS#########
                elif estado==20:
                    if self.isLetra(c) and ord(c)==73:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=21
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=73:
                            err=Error('Sintactico',fila,columna,'Se esperaba una I',c)
                            self.ListaErrores.append(err)
                elif estado==21:
                    if self.isLetra(c) and ord(c)==76:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=22
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=76:
                            err=Error('Sintactico',fila,columna,'Se esperaba una L',c)
                            self.ListaErrores.append(err)
                elif estado==22:
                    if self.isLetra(c) and ord(c)==65:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=23
                    elif self.isLetra(c) and ord(c)==84:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=23
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=65 or ord(c)!=84:
                            err=Error('Sintactico',fila,columna,'Se esperaba una A o T',c)
                            self.ListaErrores.append(err)
                elif estado==23:
                    if self.isLetra(c) and ord(c)==82:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=24
                    elif self.isLetra(c) and ord(c)==83:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=24
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isSimbolo(c) or self.isNumero(c) or ord(c)!=83 or ord(c)!=82:
                            err=Error('Sintactico',fila,columna,'Se esperaba una S o R',c)
                            self.ListaErrores.append(err)
                elif estado==24:
                    if ord(c)==61:
                        lexActual=lexActual+c
                        estado=27
                    elif self.isLetra(c) and ord(c)==79:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=25
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=61 or ord(c)!=79:
                            err=Error('Sintactico',fila,columna,'Se esperaba una O o =',c)
                            self.ListaErrores.append(err)
                elif estado==25:
                    if self.isLetra(c) and ord(c)==83:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=26
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or self.isSimbolo(c) or ord(c)!=83:
                            err=Error('Sintactico',fila,columna,'Se esperaba una S',c)
                            self.ListaErrores.append(err)
                elif estado==26:
                    if ord(c)==61:
                        contT+=1
                        token=Token(contT,tokenPalabraR,fila,columna-(len(tokenPalabraR)),'Palabra Reservada')
                        self.ListaTokens.append(token)
                        lexActual=lexActual+c
                        estado=30
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=61:
                            err=Error('Sintactico',fila,columna,'Se esperaba =',c)
                            self.ListaErrores.append(err)
                elif estado==27:
                    contT+=1
                    token=Token(contT,tokenPalabraR,fila,columna-(len(tokenPalabraR)-1),'Palabra Reservada')
                    self.ListaTokens.append(token)
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=28
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c)==False:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito',c)
                            self.ListaErrores.append(err)
                elif estado==28:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=28
                    elif ord(c)==59:
                        contT+=1
                        token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                        self.ListaTokens.append(token)
                        self.Filas.append(int(tokenNumero))
                        lexActual=lexActual+c
                        estado=29 
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o ;',c)
                            self.ListaErrores.append(err)
                elif estado==29:
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                        #err=Error('Sintactico',fila,columna - (len(lexActual) - 1),'Se espera ANCHO o ALTO o FILAS o COLUMNAS o CELDA o FILTROS',c)
                        #self.ListaErrores.append(err)
                    lexActual=''
                    tokenNumero=''
                    tokenPalabraR=''
                    estado=0
                elif estado==30:
                    if self.isLetra(c):
                        lexActual=lexActual+c
                        tokenFiltro=tokenFiltro+c
                        estado=31
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or self.isSimbolo(c) or self.isLetra(c)==False:
                            err=Error('Sintactico',fila,columna,'Se esperaba una Letra',c)
                            self.ListaErrores.append(err)
                elif estado==31:
                    if self.isLetra(c):
                        lexActual=lexActual+c
                        tokenFiltro=tokenFiltro+c
                        estado=31
                    elif ord(c)==44:
                        lexActual=lexActual+c
                        estado=32
                    elif ord(c)==59:
                        contT+=1
                        token=Token(contT,tokenFiltro,fila,columna-(len(tokenFiltro)),'Filtro')
                        self.ListaTokens.append(token)    
                        self.FiltrosAux.append(tokenFiltro) 
                        s=self.FiltrosAux.copy()
                        self.Filtros.append(s)   
                        estado=33 
                     
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=44 or ord(c)!=59:
                            err=Error('Sintactico',fila,columna,'Se esperaba una Letra o , o ;',c)
                            self.ListaErrores.append(err)
                elif estado==32:
                    contT+=1
                    token=Token(contT,tokenFiltro,fila,columna-(len(tokenFiltro)),'Filtro')
                    self.ListaTokens.append(token)
                    self.FiltrosAux.append(tokenFiltro)
                    tokenFiltro=''
                    if self.isLetra(c):
                        lexActual=lexActual
                        tokenFiltro=tokenFiltro+c
                        estado=31
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or self.isSimbolo(c) or self.isLetra(c)==False:
                            err=Error('Sintactico',fila,columna,'Se esperaba una Letra',c)
                            self.ListaErrores.append(error)
                elif estado==33:
                    self.FiltrosAux.clear()
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                        #err=Error('Sintactico',fila,columna - (len(lexActual) - 1),'Se espera ANCHO o ALTO o FILAS o COLUMNAS o CELDA o FILTROS',c)
                        #self.ListaErrores.append(err)
                    lexActual=''
                    tokenPalabraR=''
                    tokenFiltro=''
                    estado=0
                ######AQUI EMPIZA CELDAS O COLUMNAS#########
                elif estado==34:
                    if self.isLetra(c) and ord(c)==69:
                        lexActual=lexActual
                        tokenPalabraR=tokenPalabraR+c
                        estado=35
                    elif self.isLetra(c) and ord(c)==79:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=35
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=69 or ord(c)!=79:
                            err=Error('Sintactico',fila,columna,'Se esperaba E o O',c)
                            self.ListaErrores.append(err)
                elif estado==35:
                    if self.isLetra(c) and ord(c)==76:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=36
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=76:
                            err=Error('Sintactico',fila,columna,'Se esperaba una L',c)
                            self.ListaErrores.append(err)
                elif estado==36:
                    if self.isLetra(c) and ord(c)==68:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=37
                    elif self.isLetra(c) and ord(c)==85:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=37
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=68 or ord(c)==85:
                            err=Error('Sintactico',fila,columna,'Se esperaba una D o U',c)
                            self.ListaErrores.append(err)
                elif estado==37:
                    if self.isLetra(c) and ord(c)==65:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=38
                    elif self.isLetra and ord(c)==77:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=38
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=65 or ord(c)==77:
                            err=Error('Sintactico',fila,columna,'Se esperaba una A o M',c)
                            self.ListaErrores.append(err)
                elif estado==38:
                    if self.isLetra(c) or ord(c)==83:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=39
                    elif self.isLetra(c) or ord(c)==78:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=39
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=78 or ord(c)==83:
                            err=Error('Sintactico',fila,columna,'Se esperaba una S o N',c)
                            self.ListaErrores.append(err)   
                elif estado==39:
                    if self.isLetra(c) and ord(c)==65:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=40
                    elif ord(c)==61:
                        lexActual=lexActual+c
                        estado=45
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=65:
                            err=Error('Sintactico',fila,columna,'Se esperaba una A',c)
                            self.ListaErrores.append(err)
                elif estado==40:
                    if self.isLetra(c) and ord(c)==83:
                        lexActual=lexActual+c
                        tokenPalabraR=tokenPalabraR+c
                        estado=41
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isNumero(c) or ord(c)!=83:
                            err=Error('Sintactico',fila,columna,'Se esperaba una s',c)
                            self.ListaErrores.append(err)
                elif estado==41:
                    contT+=1
                    token=Token(contT,tokenPalabraR,fila,columna-(len(tokenPalabraR)-1),'Palabra Reservada')
                    self.ListaTokens.append(token)
                    if ord(c)==61:
                        lexActual=lexActual+c
                        estado=42
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=61:
                            err=Error('Sintactico',fila,columna,'Se esperaba un =',c)
                            self.ListaErrores.append(err)
                elif estado==42:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=43
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c)==False:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito',c)
                            self.ListaErrores.append(err)             
                elif estado==43:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        estado=43
                    elif ord(c)==59:
                        contT+=1
                        token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                        self.ListaTokens.append(token)
                        self.Columnas.append(int(tokenNumero))
                        estado=44
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o ;',c)
                            self.ListaErrores.append(err)
                elif estado==44:
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                    lexActual=''
                    tokenPalabraR=''
                    tokenNumero=''
                    estado=0
                elif estado==45:
                    contT+=1
                    token=Token(contT,tokenPalabraR,fila,columna-(len(tokenPalabraR)-1),'Palabra Reservada')
                    self.ListaTokens.append(token)
                    if ord(c)==123:
                        lexActual=lexActual+c
                        estado=46
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=123:
                            err=Error('Sintactico',fila,columna,'Se esperaba {',c)
                            self.ListaErrores.append(err)
                elif estado==46:
                    if ord(c)==91:
                        lexActual=lexActual+c
                        estado=47
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        elif ord(c)!=91:
                            err=Error('Sintactico',fila,columna,'Se esperaba [',c)
                            self.ListaErrores.append(err)
                elif estado==47:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        tokenX=tokenX+c
                        estado=48
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito',c)
                            self.ListaErrores.append(err)
                elif estado==48:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        tokenX=tokenX+c
                        estado=48
                    elif ord(c)==44:
                        lexActual=lexActual+c
                        estado=49
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o ,',c)
                            self.ListaErrores.append(err)
                elif estado==49:
                    contT+=1
                    token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                    self.ListaTokens.append(token)
                    tokenNumero=''
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c                       
                        tokenY=tokenY+c
                        estado=50
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o',c)
                            self.ListaErrores.append(err)
                elif estado==50:
                    if self.isNumero(c):
                        lexActual=lexActual+c
                        tokenNumero=tokenNumero+c
                        tokenY=tokenY+c
                        estado=50
                    elif ord(c)==44:
                        lexActual=lexActual+c
                        estado=51
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba un Digito o ,',c)
                            self.ListaErrores.append(err)
                elif estado==51:
                    contT+=1
                    token=Token(contT,tokenNumero,fila,columna-(len(tokenNumero)),'Numero')
                    self.ListaTokens.append(token)
                    pos=[int(tokenX),int(tokenY)]
                    self.PosicionesAux.append(pos)
                    tokenNumero=''
                    tokenX=''
                    tokenY=''
                    if self.isLetra(c) and ord(c)==70:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=52
                    elif self.isLetra(c) and ord(c)==84:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=52
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba F o T',c)
                            self.ListaErrores.append(err)
                elif estado==52:
                    if self.isLetra(c) and ord(c)==65:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=53
                    elif self.isLetra(c) and ord(c)==82:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=53
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba A o R',c)
                            self.ListaErrores.append(err)
                elif estado==53:
                    if self.isLetra(c) and ord(c)==76:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=54
                    elif self.isLetra(c) and ord(c)==85:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=54
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba L o U',c)
                            self.ListaErrores.append(err)
                elif estado==54:
                    if self.isLetra(c) and ord(c)==83:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=56
                    elif self.isLetra(c) and ord(c)==69:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=57
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba S o E',c)
                            self.ListaErrores.append(err)
                elif estado==56:
                    if self.isLetra(c) and ord(c)==69:
                        lexActual=lexActual+c
                        tokenBoolean=tokenBoolean+c
                        estado=57
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba E',c)
                            self.ListaErrores.append(err)
                elif estado==57:
                    if ord(c)==44:
                        lexActual=lexActual+c
                        estado=58
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba , ',c)
                            self.ListaErrores.append(err)
                elif estado==58:
                    contT+=1
                    token=Token(contT,tokenBoolean,fila,columna-(len(tokenBoolean)),'BOOLEAN')
                    self.ListaTokens.append(token)
                    self.BooleansAux.append(tokenBoolean) 
                    tokenBoolean=''
                    #s1=self.BooleansAux.copy()
                    #self.Booleans.append(s1)    
                    if ord(c)==35:
                        tokenColor=tokenColor+c
                        lexActual=lexActual+c
                        estado=59
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba #',c)
                            self.ListaErrores.append(err)
                elif estado==59:
                    if self.isHxdecimal(c):
                        tokenColor=tokenColor+c
                        lexActual=lexActual+c
                        estado=60
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)
                elif estado==60:
                    if self.isHxdecimal(c):
                        tokenColor=tokenColor+c
                        lexActual=lexActual+c
                        estado=61
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)
                elif estado==61:
                    if self.isHxdecimal(c):
                        tokenColor=tokenColor+c
                        lexActual=lexActual+c
                        estado=62
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)
                elif estado==62:
                    if self.isHxdecimal(c):
                        lexActual=lexActual
                        tokenColor=tokenColor+c
                        estado=63
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)      
                elif estado==63:
                    if self.isHxdecimal(c):
                        lexActual=lexActual+c
                        tokenColor=tokenColor+c
                        estado=64
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)
                elif estado==64:
                    if self.isHxdecimal(c):
                        lexActual=lexActual+c
                        tokenColor=tokenColor+c
                        estado=65
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba caracter hexadecimal',c)
                            self.ListaErrores.append(err)
                elif estado==65:
                    if ord(c)==93:
                        contT+=1
                        token=Token(contT,tokenColor,fila,columna-(len(tokenColor)),'Hexadecimal')
                        self.ListaTokens.append(token)
                        self.ColoresAux.append(tokenColor) 
                        tokenColor=''
                        lexActual=lexActual+c
                        estado=66
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba ]',c)
                            self.ListaErrores.append(err)
                elif estado==66:
                    if ord(c)==44:
                        lexActual=lexActual+c
                        estado=67
                    elif ord(c)==125:
                        lexActual=lexActual+c
                        estado=68
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba , o }',c)
                            self.ListaErrores.append(err)
                elif estado==67:
                    if ord(c)==91:
                        estado=47
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba [',c)
                            self.ListaErrores.append(err)
                elif estado==68:
                    #contT+=1
                    #token=Token(contT,tokenColor,fila,columna-(len(tokenColor)),'Hexadecimal')
                    #self.ListaTokens.append(token)
                    #self.ColoresAux.append(tokenColor) 
                    #tokenColor=''
                    if ord(c)==59:
                        Colr=self.ColoresAux.copy()
                        Bool=self.BooleansAux.copy()
                        posi=self.PosicionesAux.copy()
                        self.Booleans.append(Bool)
                        self.Posiciones.append(posi)
                        self.Colores.append(Colr)
                        lexActual=lexActual+c
                        estado=69
                    else:
                        if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                            pass
                        else:
                            err=Error('Sintactico',fila,columna,'Se esperaba ; ',c)
                            self.ListaErrores.append(err)
                elif estado==69:
                    self.ColoresAux.clear()
                    self.BooleansAux.clear()
                    self.PosicionesAux.clear()
                    if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                        pass
                    elif self.isLetra(c) or self.isSimbolo(c) or self.isNumero(c):
                        pass
                        #err=Error('Sintactico',fila,columna - (len(lexActual) - 1),'Se espera ANCHO o ALTO o FILAS o COLUMNAS o CELDA o FILTROS',c)
                        #self.ListaErrores.append(err)
                    lexActual=''
                    tokenPalabraR=''
                    estado=0   
                        
                if (ord(c) == 10):
                    columna = 0
                    fila += 1
                    continue
        # Tab Horizontal
                elif (ord(c) == 9):
                    columna += 4
                    continue
        # Espacio
                elif (ord(c) == 32):
                    columna += 1
                    continue
                columna+=1
            for a in self.ListaErrores:
                print( a.tipoError,a.descripcion,a.caracter,a.filaError,a.columnaError)

            #for ob in self.ListaTokens:
             #   print(ob.num,ob.fila,ob.columna,ob.lexema,ob.token)
            print(self.Titulos)
            #print(self.Anchos)
            #print(self.Altos)
            #print(self.Filas)
            #print(self.Columnas)
            #print(self.Posiciones)
            #print(self.Booleans)
            #print(self.Colores)
            #print(self.Filtros)
            #for i in self.ListaErrores:
             #   print (i.descripcion,i.caracter)
        
        self.Generarimagenes()
        for x in self.Titulos:
            ListaTituloGlobal.append(x)

    def GenerarTokens(self):
        pass
    def GeneraErrores(self):
        pass
    def Generarimagenes(self):

        self.Pos=[]
        for a in range(len(self.Filas)):
            for f in range(self.Filas[a]):
                for c in range(self.Columnas[a]):
                    nuevoPos=[c,f]
                    self.Pos.append(nuevoPos)
            pos1=self.Pos.copy()
            self.PosicionesTotales.append(pos1)
            self.Pos.clear()
        
        txt=''
        for i in self.Titulos:
            mkdir(f'{i}')

        for a in range(len(self.Titulos)):
            f=open(f'{self.Titulos[a]}/Original.html','w')
            txt="""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            .header {
                padding: 60px;
                text-align: center;
                 background: #2471a3 ;
                color: white;
                font-size: 30px;
                font-family:'Arial';         
            }
            body{
	        height: 100vh;            
	        display: flex; 
	        align-items: center;
	        justify-content: center;
            }
            #art{
            display:table;
            background-color:white;
            }
            #title{
	        position:absolute;
	        text-align:center;
	        font-family:Arial;
	        margin-bottom:200px;
            }
            .row{
                display:table-row;
            }
            .pixel{
            border:0.5px solid black;
            display:table-cell;
            """
            txt+=f"""
            width:{self.Anchos[a]/self.Columnas[a]}px;
            height:{self.Altos[a]/self.Filas[a]}px;
            """
            txt+="""}        
            </style>
            </head>
            <header>
             <div class="header">
            """
            txt+=f"""<h1>{self.Titulos[a]}</h1>"""
            txt+="""
            </div>
              </header>
            <body>
            <div id="art">
            """
            for filas in range(self.Filas[a]):
                txt+="""<div class="row">"""
                for columnas in range(self.Columnas[a]):
                    txt+=f"""<div class="pixel pos{columnas}_{filas}"></div>"""
                txt+="""</div>"""

            txt+="""            
            </div>
            """
            txt+="""<style>"""

            for item in range(len(self.Posiciones[a])):
                if (self.Booleans[a][item]=='TRUE'):
                    txt+=f""".pos{self.Posiciones[a][item][0]}_{self.Posiciones[a][item][1]}"""
                    txt+="""{"""
                    txt+=f"""background-color:{self.Colores[a][item]};"""
                    txt+="""}"""
                elif (self.Booleans[a][item]=='FALSE'):
                    pass
                else:
                    pass


            txt+="""</style>"""

            txt+="""
            </body>
            </html>
            """    
            f.write(txt)
            f.close()
            ###############################
            for fls in range(len(self.Filtros[a])):
                if (self.Filtros[a][fls]=='DOUBLEMIRROR'):
                    dbmirror=open(f'{self.Titulos[a]}/DoubleMirror.html','w')
                    txt2="""
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                    .header {
                    padding: 60px;
                    text-align: center;
                    background: #2471a3 ;
                    color: white;
                    font-size: 30px;
                    font-family:'Arial';         
                    }
                    body{
	                height: 100vh;            
	                display: flex; 
	                align-items: center;
	                justify-content: center;
                    }
                    #art{
                    display:table;
                    background-color:white;
                    }
                    #title{
	                position:absolute;
	                text-align:center;
	                font-family:Arial;
	                margin-bottom:200px;
                    }
                    .row{
                    display:table-row;
                    }
                    .pixel{
                    border:0.5px solid black;
                    display:table-cell;
                    """
                    txt2+=f"""
                    width:{self.Anchos[a]/self.Columnas[a]}px;
                    height:{self.Altos[a]/self.Filas[a]}px;
                    """
                    txt2+="""}        
                    </style>
                    
                        <header>
                    <div class="header">
                     """
                    txt2+=f"""<h1>{self.Titulos[a]}</h1>"""
                    txt2+="""
                    </div>
                    </header>
                    <body>
                    <div id="art">
                    """
                    #len(self.notas2)-1,-1,-1
                    for Filas in range(self.Filas[a]-1,-1,-1):
                        txt2+="""<div class="row">"""
                        for columnas in range(self.Columnas[a]-1,-1,-1):
                            txt2+=f"""<div class="pixel pos{columnas}_{Filas}"></div>"""
                        txt2+="""</div>"""

                    txt2+="""            
                    </div>
                    """
                    txt2+="""<style>"""

                    for item in range(len(self.Posiciones[a])):
                        if (self.Booleans[a][item]=='TRUE'):
                            txt2+=f""".pos{self.Posiciones[a][item][0]}_{self.Posiciones[a][item][1]}"""
                            txt2+="""{"""
                            txt2+=f"""background-color:{self.Colores[a][item]};"""
                            txt2+="""}"""
                        elif (self.Booleans[a][item]=='FALSE'):
                            pass
                        else:
                            pass


                    txt2+="""</style>"""

                    txt2+="""
                    </body>
                    </html>
                    """    
                    dbmirror.write(txt2)
                    dbmirror.close()
                elif (self.Filtros[a][fls]=='MIRRORX'):
                    mirrorX=open(f'{self.Titulos[a]}/MirrorX.html','w')
                    txt3="""
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                    .header {
                    padding: 60px;
                    text-align: center;
                    background: #2471a3 ;
                    color: white;
                    font-size: 30px;
                    font-family:'Arial';         
                    }
                    body{
	                height: 100vh;            
	                display: flex; 
	                align-items: center;
	                justify-content: center;
                    }
                    #art{
                    display:table;
                    background-color:white;
                    }
                    #title{
	                position:absolute;
	                text-align:center;
	                font-family:Arial;
	                margin-bottom:200px;
                    }
                    .row{
                    display:table-row;
                    }
                    .pixel{
                    border:0.5px solid black;
                    display:table-cell;
                    """
                    txt3+=f"""
                    width:{self.Anchos[a]/self.Columnas[a]}px;
                    height:{self.Altos[a]/self.Filas[a]}px;
                    """
                    txt3+="""}        
                    </style>
                    </head>
                     <header>
                    <div class="header">
                     """
                    txt3+=f"""<h1>{self.Titulos[a]}</h1>"""
                    txt3+="""
                    </div>
                    </header>
                    <body>
                    <div id="art">
                    """
                    #len(self.notas2)-1,-1,-1
                    for Filas in range(self.Filas[a]):
                        txt3+="""<div class="row">"""
                        for columnas in range(self.Columnas[a]-1,-1,-1):
                            txt3+=f"""<div class="pixel pos{columnas}_{Filas}"></div>"""
                        txt3+="""</div>"""

                    txt3+="""            
                    </div>
                    """
                    txt3+="""<style>"""

                    for item in range(len(self.Posiciones[a])):
                        if (self.Booleans[a][item]=='TRUE'):
                            txt3+=f""".pos{self.Posiciones[a][item][0]}_{self.Posiciones[a][item][1]}"""
                            txt3+="""{"""
                            txt3+=f"""background-color:{self.Colores[a][item]};"""
                            txt3+="""}"""
                        elif (self.Booleans[a][item]=='FALSE'):
                            pass
                        else:
                            pass
                    txt3+="""</style>"""
                    txt3+="""
                    </body>
                    </html>
                    """    
                    mirrorX.write(txt3)
                    mirrorX.close()
                elif (self.Filtros[a][fls]=='MIRRORY'):
                    mirrorY=open(f'{self.Titulos[a]}/MirrorY.html','w')
                    txt4="""
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                     .header {
                    padding: 60px;
                    text-align: center;
                    background: #2471a3 ;
                    color: white;
                    font-size: 30px;
                    font-family:'Arial';         
                    }
                    body{
	                height: 100vh;            
	                display: flex; 
	                align-items: center;
	                justify-content: center;
                    }
                    #art{
                    display:table;
                    background-color:white;
                    }
                    #title{
	                position:absolute;
	                text-align:center;
	                font-family:Arial;
	                margin-bottom:200px;
                    }
                    .row{
                    display:table-row;
                    }
                    .pixel{
                    border:0.5px solid black;
                    display:table-cell;
                    """
                    txt4+=f"""
                    width:{self.Anchos[a]/self.Columnas[a]}px;
                    height:{self.Altos[a]/self.Filas[a]}px;
                    """
                    txt4+="""}        
                    </style>
                    </head>
                    <header>
                    <div class="header">
                    """
                    txt4+=f"""<h1>{self.Titulos[a]}</h1>"""
                    txt4+="""
                    </div>
                    </header>
                    <body>
                    <div id="art">
                    """
                    #len(self.notas2)-1,-1,-1
                    for Filas in range(self.Filas[a]-1,-1,-1):
                        txt4+="""<div class="row">"""
                        for columnas in range(self.Columnas[a]):
                            txt4+=f"""<div class="pixel pos{columnas}_{Filas}"></div>"""
                        txt4+="""</div>"""

                    txt4+="""            
                    </div>
                    """
                    txt4+="""<style>"""

                    for item in range(len(self.Posiciones[a])):
                        if (self.Booleans[a][item]=='TRUE'):
                            txt4+=f""".pos{self.Posiciones[a][item][0]}_{self.Posiciones[a][item][1]}"""
                            txt4+="""{"""
                            txt4+=f"""background-color:{self.Colores[a][item]};"""
                            txt4+="""}"""
                        elif (self.Booleans[a][item]=='FALSE'):
                            pass
                        else:
                            pass
                    txt4+="""</style>"""
                    txt4+="""
                    </body>
                    </html>
                    """    
                    mirrorY.write(txt4)
                    mirrorY.close()
                



    

        




                
            





        