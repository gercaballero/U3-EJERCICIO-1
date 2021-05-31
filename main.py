from classManejadorLibros import ManejadorLibros
from classMenu import Menu
import os
if __name__=='__main__':
    ml=ManejadorLibros()
    ml.cargar()
    ml.listar()
    input()
    os.system('cls')
    menu=Menu()

    salir= False           
    while not salir:
            print("\n-------------------Menu-------------------")
            print(' 1- MOSTRAR LIBRO POR ID')
            print(' 2- PALABRA EN TITULO')
            print(' 3- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3'):
                menu.opcion(int(op),ml)
                if op=='3':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
