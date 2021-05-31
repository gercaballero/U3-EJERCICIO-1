
class Capitulo:
    __titulo=''
    __cantPaginas=0

    def __init__(self,titulo,paginas):
        self.__titulo=titulo
        self.__cantPaginas=paginas
    
    def __str__(self):
        return ('TITULO:{}\tPAGINAS:{}'.format(self.__titulo,self.__cantPaginas))
    
    def getTitulo(self):
        return self.__titulo