from claseManejador import claseManejador
from claseManejadorMateria import ManejadorMateria
from menuOpciones import Menu

if __name__ == '__main__':
    a = claseManejador()
    a.cargarArreglo()
    arreglo = a.getArreglo()
    m = ManejadorMateria()
    m.testMaterias()
    print('\n Materias aprobadas:\n')
    print(m)
    ban = True
    while ban:
        op = Menu.select(a, m)
        if op == "0":
            ban = False
        elif op != "1" and op != "2" and op != "3":
            print("Opcion no valida. Intente nuevamente")

    #if posicion == None:
    #    print('\nEl DNI no está registrado. Intente nuevamente\n')
