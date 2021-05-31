import os
from classManejadorLibros import ManejadorLibros

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op,ml):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(ml)

    def salir(self,ml):
        print('Salida del programa')

    def opcion1(self,ml):
        id=int(input('INGRESE IDENTIFICADOR DE UN LIBRO: '))
        if ml.mostrarPorId(id)==False:
            pass
        else:
            print('ID DE LIBRO NO ENCONTRADO')
        input()
        os.system('cls')

    def opcion2(self,ml):
        palabra=input('INGRESE PALABRA QUE DESEA BUSCAR EN ALGUN TITULO: ')
        if not ml.mostrarPorPalabra(palabra.upper()):
            pass
        else:
            print('LA PALABRA ´´{}´´ NO SE ENCUENTRA EN NINGUN LIBRO'.format(palabra.upper()))
        input()
        os.system('cls')
