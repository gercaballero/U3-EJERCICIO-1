from classCapitulo import Capitulo
from classLibro import Libro
import csv
import re

class ManejadorLibros:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarLibro(self,unLibro):
        if isinstance(unLibro, Libro):
            self.__lista.append(unLibro)
    
    def agregarCapitulo(self,unCapitulo):
        if isinstance(unCapitulo, Capitulo):
            self.__lista[len(self.__lista)-1].agregarCapitulo(unCapitulo)

    def cargar(self):
        archivo=open('libros.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if fila[0].isdigit():
                id=int(fila[0])
                titulo=fila[1]
                autor=fila[2]
                editorial=fila[3]
                isbn=int(fila[4])
                cantCapitulos=int(fila[5])
                unLibro=Libro(id, titulo, autor, editorial, isbn, cantCapitulos)
                self.agregarLibro(unLibro)
            else:
                titulo=fila[0]
                paginas=int(fila[1])
                unCapitulo=Capitulo(titulo, paginas)
                self.agregarCapitulo(unCapitulo)

    def listar(self):
        for libro in self.__lista:
            print('\n')
            print(libro)

    def mostrarPorId(self,id):
        band=True
        i=0
        while band and i<len(self.__lista):
            if self.__lista[i].getId()==id:
                self.__lista[i].mostrar()
                band=False
            else:
                i+=1
        return band

    def mostrarPorPalabra(self,palabra):
        band=True
        for libro in self.__lista:
            if libro.palabraEnTitulo(palabra)==False:
                print('\t TITULO:{}\t AUTOR:{}'.format(libro.getTitulo(),libro.getAutor()))
                band=False
        return band
            
