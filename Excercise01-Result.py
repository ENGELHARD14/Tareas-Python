listaRegistro = []
clientes = 0


while clientes < 1972972:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    detener = input("Ingresar la palabra si para detener ")
    if detener == ("si"):
        break
    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    clientes += 1

"""

    Costos = float(sum(costo))
    print(costo)
"""

for registro in listaRegistro:
    print(registro)