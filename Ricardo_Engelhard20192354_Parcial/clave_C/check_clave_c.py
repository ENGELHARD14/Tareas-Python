from clave_c import (
    multiplicar,
    sumaDivTresYCinco,
    definicionCono,
    Cono,
    CentroMedico,
    Paciente,
    getGithubUrl,
)

print("Clave C...")


# ejercicio 1 -->
result = multiplicar()
if result == 8:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")


# ejercicio 2 -->
result = sumaDivTresYCinco()
if result == 33165:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")


# ejercicio 3 -->
result = definicionCono()
if result == {
    "generatriz": 12.083045973594572,
    "area": 268.33985865790703,
    "volumen": 287.9793265790644,
}:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")


# ejercicio 4 -->
cono = Cono()
result = cono.definicionCono()
if result == {
    "generatriz": 12.083045973594572,
    "area": 268.33985865790703,
    "volumen": 287.9793265790644,
}:
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")


# ejercicio 5 -->
centroMedico = CentroMedico()
# centroMedico.registrar(Paciente("balbino", "san salvador", "gripe", 40.0, False, 0.0))
# centroMedico.registrar(Paciente("marta", "santa ana", "dolor cabeza", 30.0, True, 5.0))
# centroMedico.registrar(Paciente("rodrigo", "san salvador", "golpe", 50.0, False, 0.0))
# centroMedico.registrar(Paciente("jaime", "la libertad", "gripe", 40.0, True, 10.0))
# centroMedico.registrar(
#     Paciente("balbino", "la libertad", "dol estomago", 30.0, False, 0.0)
# )
# centroMedico.registrar(Paciente("marta", "san salvador", "mareo", 20.0, True, 5.0))
# centroMedico.registrar(Paciente("karen", "san salvador", "gripe", 40.0, False, 0.0))
# ejemplos
result = centroMedico.totalCostoSanSalvador()
if result == "$150.00":
    print("ejercicio05part01: pass")
else:
    print("ejercicio05part01: fail")

result = centroMedico.totalCostoConDescuento()
if result == "$230.00":
    print("ejercicio05part02: pass")
else:
    print("ejercicio05part02: fail")


# ejercicio 6 -->
result = getGithubUrl()
if not result == "":
    print("ejercicio06: pass")
else:
    print("ejercicio06: fail")
