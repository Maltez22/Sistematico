#listas
listas = [1, 2, 3, "Manzana", 15.6, True]
print(listas)

#imprimir el primer elemento de la lista
print(listas[0])

#tamano de la lista
tam = len(listas)
print(f"el tamano es {tam}")

#imprimir el ultimo valor
print(listas[tam-1])

#imprimir los primeros elementos
print(listas[0:3])
#imprimir los elementos del 4 al 6
print(listas[3:7])
#agregar un elemento a la lista
listas.append("Luis")
print(listas)
#imprimir los ultimos 3 elementos de la lista
final = len(listas)
inicio = final - 3
print(listas[inicio: final +1])

#wliminar Manzana
listas.remove("Manzana")
listas.remove("Luis")


#ordenar lista
listas.sort()
print(listas)