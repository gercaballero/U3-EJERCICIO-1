from classCapitulo import Capitulo
import re
class Libro:
    __idLibro=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantCapitulos=0
    __capitulos=[]
    
    def __init__(self,id,titulo,autor,editorial,isbn,cantCapitulos):
        self.__idLibro=id
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=editorial
        self.__cantCapitulos=cantCapitulos
        self.__capitulos=[]
    
    def agregarCapitulo(self,capitulo):
        if isinstance(capitulo, Capitulo):
            self.__capitulos.append(capitulo)
        
    def __str__(self):
        libro=('ID:{} TITULO:{} AUTOR:{} EDITORIAL:{} ISBN:{} CANT.CAPITULOS:{}\n\tCAPITULOS:'.format(self.__idLibro,self.__titulo,self.__autor,self.__editorial,self.__isbn,self.__cantCapitulos))
        capitulos=''
        for capitulo in self.__capitulos:
            capitulos=capitulos+('\n\t\t~{}'.format(capitulo))
        return libro+capitulos

    def mostrar(self):
        print('TITULO:{}'.format(self.__titulo))
        for capitulo in self.__capitulos:
            print('\t\t{}'.format(capitulo))

    def palabraEnTitulo(self,palabra):
        band=True
        i=0
        if re.search(palabra,self.__titulo.upper()):    #Busca si la palabra se encuentra en el titulo del libro
                band=False
        if band:
            while band and i<len(self.__capitulos):
                #Busca si la palabra se encuentra en los titulos de los capitulos
                if re.search(palabra,self.__capitulos[i].getTitulo().upper()):
                    band=False
                else:
                    i+=1
        return band
    def __del__(self):
        print('BORRANDO CAPITULOS')
        del self.__capitulos

    def getAutor(self):
        return self.__autor
    def getId(self):
        return int(self.__idLibro)
    def getTitulo(self):
        return self.__titulo