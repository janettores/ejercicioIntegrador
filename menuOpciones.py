class Menu:
    __opcion = ''
    def select (self, a, m):

        print("Menu:")
        print("1 - Promedio con y sin aplazos")
        print("2 - Listado alumnos promocionales")
        print("3 - Listado de alumnos")
        print("0 - Salir")
        self.__opcion = input("Elija una opcion: ")

        if self.__opcion == "1":
            dni = input("Ingrese el DNI del alumno: ")
            alumno = a.buscarAlumno(dni)
            if alumno == None:
                print("No se encontro el alumno")
            else:
                m.calculopromedio(dni)

        elif self.__opcion == "2":
            materia = input("Ingrese el nombre de la materia: ")
            print(f"Listado de alumnos promocionales de la materia {materia}")
            m.promocionales(a, materia)
            print("")

        elif self.__opcion == "3":
            a.ordenar()

        return self.__opcion