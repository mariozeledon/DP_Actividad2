num=[]
for i in range(10):
    num.append(input("Ingrese un numero: "))

def mayor(num):
    max = num[0];
    for x in num+1:
        if x > max:
            max = x
    return max    

print( "\nEl numero mayor es: ",max(num))    

def menor(num):
    min = num[0];
    for x in num+1:
        if x < min:
            min = x
    return min    

print("El numero menor es: ",min(num))

num.sort()
print("Orden de forma ascendente: ",num)

myNewList = [int(string) for string in num]
sum1 = sum(myNewList)

print("El resultado de la suma es: ",sum1)

