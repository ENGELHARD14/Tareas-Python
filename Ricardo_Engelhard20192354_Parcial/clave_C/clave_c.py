import math
from math import sqrt

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar():
    mult = 2 * 4
    return mult


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    result = 0
    suma = 0
    while result < 1000:
        if (result % 3 == 0) and (result % 5 == 0):
            suma = result + suma
        result += 1
    return suma


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
# diccionarioCono
def definicionCono():
    generatriz = obtenerGeneratriz()
    area = obtenerArea()
    volumen = obtenerVolumen()
    result = {"generatriz": generatriz, "area": area, "volumen": volumen}
    return result


def obtenerGeneratriz():
    result = math.sqrt((11 ** 2) + (5 ** 2))
    return result


def obtenerArea():
    result = math.pi * 5 * (5 + obtenerGeneratriz())
    return result


def obtenerVolumen():
    result = (1 / 3) * math.pi * (5 ** 2) * 11
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""

# start-->
class Cono:
    def definicionCono(self):
        return definicionCono()

    def definicionCono(self):
        generatriz = obtenerGeneratriz()
        area = obtenerArea()
        volumen = obtenerVolumen()
        result = {"generatriz": generatriz, "area": area, "volumen": volumen}

        return result

    def obtenerGeneratriz(self):
        result = math.sqrt((11 * 2) + (5 * 2))
        return result

    def obtenerArea(self):
        result = math.pi * 5 * (5 + obtenerGeneratriz())
        return result

    def obtenerVolumen(self):
        result = (1 / 3) * math.pi * (5 ** 2) * 11
        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""
# centroMedico.registrar(Paciente("balbino", "san salvador", "gripe", 40.0, False, 0.0))
# centroMedico.registrar(Paciente("marta", "santa ana", "dolor cabeza", 30.0, True, 5.0))
# centroMedico.registrar(Paciente("rodrigo", "san salvador", "golpe", 50.0, False, 0.0))
# centroMedico.registrar(Paciente("jaime", "la libertad", "gripe", 40.0, True, 10.0))
# centroMedico.registrar(
# Paciente("balbino", "la libertad", "dol estomago", 30.0, False, 0.0))
# centroMedico.registrar(Paciente("marta", "san salvador", "mareo", 20.0, True, 5.0))
# centroMedico.registrar(Paciente("karen", "san salvador", "gripe", 40.0, False, 0.0))


class CentroMedico:
    def __init__(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.name = nombre
        self.lugar = lugar
        self.descripcion = descripcion
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento

    def totalCostoSanSalvador(self):
        self.costo = True

    def totalCostoConDescuento(self):
        self.conDescuento = True


# p1 = Paciente("balbino", "san salvador", "gripe", 40.0, False, 0.0)
# p2 = Paciente("marta", "santa ana", "dolor cabeza", 30.0, True, 5.0)


class Paciente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    url = "https://github.com/ENGELHARD14/Tareas-Python.git"
    return url
