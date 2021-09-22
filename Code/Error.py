class Error:
    def __init__(self,tipo,filaEr,columnaEr,des,caracter):
        self.tipoError=tipo
        self.filaError=filaEr
        self.columnaError=columnaEr
        self.descripcion=des
        self.caracter=caracter
