class Alumno:
    slots = [__NP, __nombreCompleto, __notaMedia]

    def __init__(self, NP=None, nombreCompleto=None, notaMedia=None):
        __NP=0
        __nombreCompleto= "A B C"
        __notaMedia= 0.0
        if(NP is not None and isinstance(NP, int)):
            __NP=NP
        if(nombreCompleto is not None and isinstance(nombreCompleto, str)):
            __nombreCompleto= nombreCompleto
        if(notaMedia is not None and isinstance(notaMedia, float)):
            __notaMedia= notaMedia


    def get_NP(self):
        return self.__NP

    def get_nombreCompleto(self):
        return self.__nombreCompleto

    def get_notaMedia(self):
        return self.__notaMedia


    @getNP.setter
    def setNP(self, NP):
        self.__NP = NP

    @getNP.setter
    def setNombreCompleto(self, nombreCompleto):
        self.__nombreCompleto = nombreCompleto

    @getNP.setter
    def setNotaMedia(self, notaMedia):
        self.__notaMedia = notaMedia
