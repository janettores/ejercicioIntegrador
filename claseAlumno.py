class Alumno:
    __dni = ''
    __apellido = ''
    __nombre = ''
    __carrera = ''
    __aniocarrera= 0

    def __init__(self, dni = '', apellido = '', nombre = '', carrera = '', aniocarrera= ''):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__aniocarrera = aniocarrera

    def __str__(self):
        return f'[DNI: {self.__dni}, Apellido: {self.__apellido}, Nombre: {self.__nombre}, Carrera:{self.__carrera},Año de carrera:{self.__aniocarrera}]'

