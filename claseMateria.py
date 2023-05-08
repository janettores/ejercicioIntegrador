class Materia:
    __dni = ''
    __nombremateria = ''
    __fecha = ''
    __nota = 0
    __aprobacion = ''

    def __init__(self, dni = '', nombremateria = '', fecha = '', nota = 0, aprobacion = ''):
        self.__dni = dni
        self.__nombremateria = nombremateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def __str__(self) -> str:
        return f'[DNI del alumno: {self.__dni},Materia: {self.__nombremateria},Fecha:{self.__fecha},Nota:{self.__nota}, Aprobacion:{self.__aprobacion}]'

    def getDni(self):
        return self.__dni

    def getNota(self):
        return self.__nota
