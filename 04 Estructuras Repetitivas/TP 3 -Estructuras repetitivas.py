"""
EJERCICIO 1
"""
#Se inicializa la variable
num_ent = 0

#Se imprimen los numeros desde el 0 al 100
for num_ent in range (0, 101):
    print(num_ent)

"""
EJERCICIO 2
"""
num_ent = int(input("Ingrese un numero entero: "))
cant_digitos = len(str(num_ent))
contador = 0

if num_ent == 0:
    contador = 1
else:
    while num_ent > 0:
        num_ent //= 10
        contador += 1

print(f"El numero tiene {contador} digito(s)")

"""
EJERCICIO 3
"""
#Solicitar dos números al usuario
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

#Inicializar la suma
suma = 0

#Sumar los números entre los dos valores, excluyendo ambos
for i in range(inicio + 1, fin):
    suma += i

#Mostrar el resultado
print(f"La suma de los números enteros entre {inicio} y {fin}, es: {suma}")

"""
EJERCICIO 4
"""
#Se inicializa la variable para calcular la suma  
suma_total = 0
num_ent = int(input("Ingrese un numero entero: "))

#Bucle while para sumar los numeros ingresados
while num_ent > 0:
    suma_total += num_ent
    num_ent = int(input("Ingrese otro numero entero (0 para terminar): "))
if num_ent == 0:
    print(f"La suma total es: {suma_total}")

"""
EJERCICIO 5
"""
import random
#Se genera un numero aleatorio con random entre 0 y 9
num_aleatorio = random.randint(0, 9)

#Se le pide al usuario que adivine
num_usuario = int(input("Adivina el numero entre 0 y 9: "))

#Se inicializa el contador de los intentos
intentos = 0

#Bucle while para adivinar el numero
while num_aleatorio != num_usuario:
    intentos += 1
    num_usuario = int(input("Intenta de nuevo!"))
if num_usuario == num_aleatorio:
    print(f"Felicidades! Adivinaste el numero en {intentos} intento(s)")   

"""
EJERCICIO 6
"""
#Bucle for para contar en forma decreciente de 100 a 0 y solo recorriendo los numeros pares
for num_par in range (100, -1, -2):
    print(num_par)

"""
EJERCICIO 7
"""
#Se inicializa la suma 
suma = 0
#Se le pide al usuario un numero 
num_usuario = int(input("Ingrese un numero mayor a 0: "))

#Bucle for para sumar los numeros 
for i in range (num_usuario + 1):
    suma += i
    
print(f"La suma de los numeros de 0 a {num_usuario}: {suma}")

"""
EJERCICIO 8
"""
#Se le piden 100 numeros al usuario
numeros = 100
#Se inicializan las variables
pares = 0
impares = 0
negativos = 0
positivos = 0

print("Ingresa 100 numeros enteros")

for i in range (numeros):
    numero = int(input(f"Numero {i+1}: "))
    
    #Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    #Positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")

"""
EJERCICIO 9
"""
#Cantidad de números a ingresar
cantidad = 100  

#Acumulador para la suma
suma = 0

print(f"Ingresa 100 numeros enteros: ")

for i in range(cantidad):
    numero = int(input(f"Numero {i+1}: "))
    suma += numero

#Calcular la media
media = suma / cantidad

print(f"\nLa media de los 100 numeros ingresados es: {media}")

"""
EJERCICIO 10
"""
numero = int(input("Ingresa un número entero: "))
inverso = 0

while numero > 0:
    digito = numero % 10
    inverso = inverso * 10 + digito
    numero = numero // 10

print(f"El número invertido es: {inverso}")