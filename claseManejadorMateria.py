from claseMateria import Materia
import csv

class ManejadorMateria:
    __lista = []

    def __init__(self):
        self.__lista = []        #creo una lista vacia
    def agregarMateria(self, mat_aprob):
        self.__lista.append(mat_aprob)        #agrego el objeto materia (con los datos del archivo) en la lista creada
        #print(mat_aprob.__str__())

    def __str__(self):
        s = ''
        for materia in self.__lista:
            s += str(materia) + '\n'
        return s

    def promedioconaplazo(self, dni):
        cont = 0
        nota = 0.0
        prom = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni() == dni:
                nota += self.__lista[i].getNota()
                cont += 1
                prom = nota/cont
        return (prom)
    def promediosinaplazo(self, dni):
        cont = 0
        nota = 0.0
        prom = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDni() == dni:
                if self.__lista[i].getNota() > 4:
                    nota += self.__lista[i].getNota()
                    cont += 1
                    prom = nota/cont
        return (prom)
    def calculopromedio(self, dni):
        print('\nEl promedio del alumno con aplazos es: ', self.promedioconaplazo(dni))
        print('\nEl promedio del alumno sin aplazos es:', self.promediosinaplazo(dni))

    def promocionales(self, a, materia):
        ban = 0
        for m in self.__lista:
            if m.getNombre() == materia:
                if m.getAprobacion() == "P":
                    dni = m.getDNI()
                    alumno = a.buscarAlumno(dni)
                    ban = 1
                    print(
                        f"{dni}, {alumno.getApellido()} {alumno.getNombre()}, {m.getFecha()}, {m.getNota()}, {alumno.getAño()}")

        if ban == 0:
            print("No hubo alumnos promocionales en esta materia")
    def testMaterias(self):
        archivo = open('materiasAprobadas', 'r')
        reader = csv.reader(archivo, delimiter=';')      #reader es un iterable de la clase csv.reader
        next(reader)
        for fila in reader:
            mat_aprob = Materia(fila[0], fila[1], fila[2], int(fila[3]), fila[4])
            self.agregarMateria(mat_aprob)
        archivo.close()






    '''def buscaralumno(self,dni):
        indice = 0
        a = 0
        s = 0
        valorDeRetorno = None
        while indice < len(self.__lista):
            if self.__lista[indice].getDni() == dni:
                valorDeRetorno = indice
                a += 1
                totalconaplazo = ManejadorMateria.promedioconaplazo(indice)
                if self.__lista[indice].getNota() > 4:
                    s += 1
                    totalsinAplazo = ManejadorMateria.promediosinaplazo(indice)
            else:
                indice += 1
        return valorDeRetorno'''
