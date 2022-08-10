tupla=("Uno","Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho")
print("A. Mostrar un elemento por línea")
for i in range(len(tupla)):
    print(tupla[i])

print("\n\nB. Mostrar todas las letras en mayúscula.")
for i in range(len(tupla)):
    print(tupla[i].upper())

print("\n\nC. Mostrar todas las letras en minúscula.")
for i in range(len(tupla)):
    print(tupla[i].lower())

print("\n\nD. Mostar los textos que finalizan con la letra “s”.")
for i in range(len(tupla)):
   if(tupla[i][len(tupla[i])-1:len(tupla[i])]) == "s" or (tupla[i][len(tupla[i])-1:len(tupla[i])]) == "S":
       print(tupla[i])
a=0
e=0
vocali=0
o=0
u=0
print("\n\nE. Contar la cantidad de vocales existentes en los textos")
for i in range(len(tupla)):
    for x in range(len(tupla[i])):
        if(tupla[i][x:x+1]) == "a" or (tupla[i][x:x+1]) == "A":
            a+=1
        if(tupla[i][x:x+1]) == "e" or (tupla[i][x:x+1]) == "E":
            e+=1
        if(tupla[i][x:x+1]) == "i" or (tupla[i][x:x+1]) == "I":
            vocali+=1
        if(tupla[i][x:x+1]) == "o" or (tupla[i][x:x+1]) == "O":
            o+=1
        if(tupla[i][x:x+1]) == "u" or (tupla[i][x:x+1]) == "U":
            u+=1
print ("a = ",a)
print ("e = ",e)
print ("i = ",vocali)
print ("o = ",o)
print ("u = ",u)
