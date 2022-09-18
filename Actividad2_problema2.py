lista = []
for i in range(15):
    lista.append(input("Ingrese un texto: "))
    
lista.sort()
print("Orden de forma ascendente: ",lista)

lista.sort(reverse=True)
print("Ordenar de forma descendente: ",lista)

longitud=int(0)
for x in range(15):    
    longitud = (len(lista[x]))+longitud

promedio = longitud/3

print("El promedio de las longitudes de los nombres es: ",promedio)

