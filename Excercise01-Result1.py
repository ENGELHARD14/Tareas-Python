listaRegistro = []
clientes = 0
costos=0


while clientes < 1972972:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    costos += costo

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    listaRegistro.append(registro)
    
    detener = input("Escribir '+' para agregar datos, escribir lo que sea para detener ")
    if detener == ("+"):
	    clientes += 1
    else:
        break
        
        
for registro in listaRegistro:
    print(registro)
	
print(costos)

   
   
   
""""clientes += 1



    Costos = float(sum(costo))
    print(costo)


for registro in listaRegistro:
    print(registro)
"""