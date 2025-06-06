class Alumno:
    __slots__ = ['__NP', '__nombreCompleto', '__notaMedia']

    def __init__(self, NP=None, nombreCompleto=None, notaMedia=None):
        self.__NP=0
        self.__nombreCompleto= "A B C"
        self.__notaMedia= 0.0
        if(NP is not None and isinstance(NP, int)):
            self.__NP=NP
        if(nombreCompleto is not None and isinstance(nombreCompleto, str)):
            self.__nombreCompleto= nombreCompleto
        if(notaMedia is not None and isinstance(notaMedia, float)):
            self.__notaMedia= notaMedia

    def getNP(self):
        return self.__NP

    def setNP(self, NP):
        self.__NP = NP

    def getNombreCompleto(self):
        return self.getNombreCompleto

    def setNombreCompleto(self, nombreCompleto):
        self.__nombreCompleto = nombreCompleto

    def getNotaMedia(self):
        return self.__NP

    def setNotaMedia(self, notaMedia):
        self.__notaMedia = notaMedia


    def __str__(self):
        #return ("" + str(self.__NP))
        return f"({self.__NP}, {self.__nombreCompleto}, {self.__notaMedia})"
    
#    def __eq__(self, other): #Permite utilizar el símbolo == entre objetos de tipo Alumno
#        if isinstance(other, Alumno):
#            return self.__NP == other.__NP
#        return False
    
    def equals(self, other):  
        if isinstance(other, Alumno):
            return self.__NP == other.__NP
        return False


a1=Alumno()
print("a1:", a1)  #Puedo poner a1 directamente porque está definido el método especial __str__

a2=Alumno(10) #Indicamos un valor sólo para __NP
print("a2:", a2)

a3=Alumno("Pedro García López") #Indicamos un valor sólo para __nombreCompleto
print("a3:", a3)                #Asimila la cadena a NP y como no es int, no aplica

a3=Alumno(None, "Pedro García López") #Indicamos un valor sólo para __nombreCompleto
print("a3:", a3)                #Ahora sí se asimila "Pedro...." con __nombreCompleto

print (f"a1 igual a3?: {a1 == a3}") # Al haber quitado el método __eq__ compara el contenido de las
                                    # referencias y como son objetos diferentes da False

print (f"a1 igual a3?: {a1.equals(a3)}") # Como equals comprueba que los NPs sean iguales, 
                                         #devuelve True