def mayor_de_tres(a,b,c):
    if a > b and a > c:
        return f"{a} es el mayor de los tres numeros"
    elif b > a and b > c:
        return f"{b} es el mayor de los tres numeros"
    else:
        return f"{c} es el mayor de los tres numeros"

num1 = input("ingrese el primer numero: ")
num2 = input("ingresa el segundo numero ")
num3 = input("ingresa el tercer numero: ")

resultado = mayor_de_tres(num1,num2,num3)
print("el mayor de los tres numeros es: ",resultado)


def vocales(cadena):
    vocales = 'aeiouAEIOU'
    count = 0
    for i in cadena:
        if i in vocales:
            count +=1
    return count

cadena = input("ingresa una palabra: ")
resultado = vocales(cadena)
print(f"la antidad de vocales que hay en la palabra que ingresaste es{resultado}")

pi = 3.1416

def area_circulo(radio):
    return pi * radio**2

radio = float(input("ingrese el radio del circulo: "))
resultado = area_circulo(radio)
print(f"el area del circulo es: {resultado}")

for i in range (1,11):
        print(i)


numero = int(input("ingrese un numero:"))
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


numero = int(input("ingrese un numero cualquiera:"))
suma = 0
for i in range(1, numero + 1):
    suma += i
print  (f"la suma de numero es: {suma}")

numero = int(input("ingrese un numero"))
fac = 1
for i in range(1,numero + 1):
    fac *= i
print(f"el resultado del numero factoria es:{fac}")


vector = [1, 2, 3, 4, 5, 6]
vector[5] = 10
print(vector[0])
print(vector)

for i in vector:
    print(i)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz[1][1] = 50
for i in matriz:
    for e in i:
        print(e, end=" ")
print()

vec = []

for i in range(3):
    numero = int(input("ingresa un numero: "))
    vec.append(numero)
print(vec)

vector = [1, 2, 3, 4, 5, 6, 7]
suma = 0
for i in vector:
    suma = suma + i  # esto es igual a suma += i
print("la suma de los numero de los vectores es: ", suma)

vector = []

for i in range(5):
    numero = int(input("ingrese un numero: "))
    vector.append(numero)
mayor = [0]
for numero in vector:
    if numero > mayor:
        mayor = numero
print("el numero mayor es:", mayor )


numero = int(input("ingrese un numero entero: "))
resultado = 0
for i in range(1, numero + 1):
    resultado += i
print("la suma de tu numero hasta 1 es: ",resultado)

word = input("ingrese una palabra")
palindromo = ""
len_word = len(word)-1
for i in range(len(word)):
    palindromo = palindromo + word[len_word]
    len_word = len_word - 1
if word == palindromo:
    print(True)
else:
    print(False)

number = int(input("ingrese un numero: "))
suma = 0
for i in range(1,number-1):
    if number% 3 == 0 or number% 5 == 0:
        suma += i
print(suma)

vector = [["hola"], ["mundo"], ["soy un chanchito feliz"]]

for i in range()


numero = int(input("ingrese un numero: "))


def es_primo(numero):
    if numero <= 1:
        return False
    for divisor in range(2,numero):
        if numero % divisor == 0:
            return False
    return True

if es_primo(numero):
    print(f"el numero que ingresaste es primo: {numero}")
else:
    print(f"el numero que ingresaste no es primo: {numero}")

vec1 = [1, 2, 4]
vec2 = [4, 5, 6]

vec_sum = []

for i in range(len(vec1)):
    sum = vec1[i] + vec2[i]
    vec_sum.append(sum)
print(vec_sum)


matriz = [
    [1, 2],
    [3, 4]
]
subir = 2
resultado = []
for fila in matriz:
    new_row = []
    for elemento in fila:
        new_row.append(elemento * subir)
    resultado.append(new_row)
print(resultado)


matriz = [
    [1],
    [2]
]
for i in matriz:
    for j in matriz[0]:
        print("hola")
