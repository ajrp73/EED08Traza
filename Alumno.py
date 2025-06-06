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
        
    def __str__(self):
        return f"({self.__NP},{self.__nombreCompleto}, {self.__notaMedia})"