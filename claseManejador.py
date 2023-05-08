from claseAlumno import Alumno
import numpy as np
import csv

class claseManejador:      #clase controlador del arreglo de alumnos
    __indice     = 0
    __dimension  = 0
    __incremento = 5
    __arreglo    = None

    def __init__(self, dimension = 0, incremento = 5):
        self.__arreglo   = np.empty(12, dtype=Alumno)   #creo un arreglo vacio
        self.__indice    = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def getArreglo(self):
        return self.__arreglo
    def agregarAlumno(self, instancia):
        self.__arreglo[self.__indice] = instancia
        self.__indice += 1

    def cargarArreglo(self):
        archivo = open('alumnos.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        lineadelarchivo = sum(1 for row in reader)
        self.__dimension = lineadelarchivo
        archivo.seek(0)
        print('\nLa dimension del arreglo es:', self.__dimension, '\n')
        next(reader)
        for fila in reader:
            instancia = Alumno(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.agregarAlumno(instancia)
            print(instancia)
        archivo.close()
    def buscarAlumno(self, dni):
        alumno = None
        i = 0
        while alumno == None and i < len(self.__arreglo):
            if self.__arreglo[i].getDNI() == dni:
                alumno = self.__arreglo[i]
            i += 1

        return alumno
    def ordenar(self):

        self.__arreglo.sort()

        print("Listado de alumnos:")
        for alumno in self.__arreglo:
            print(alumno)
        print("")
