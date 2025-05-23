#EJERCICIO 1
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un numero entero positivo: "))

if num < 1:
    print("Por favor, ingrese un numero mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {num}")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

'''
#EJERCICIO 2
'''
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)
    
cant_term = int(input("Ingrese la cantidad de terminos que desea mostrar: "))

print("Serie de Fibonacci: ")
for i in range(cant_term):
    print(fibonacci(i), end =" ")

'''
#EJERCICIO 3
'''
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente < 0:
    print("El exponente debe ser un numero entero positivo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

'''
#EJERCICIO 4
'''
def dec_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return dec_binario(n // 2) + str(n % 2)
    
num = int(input("Ingresa un numero entero positivo: "))

if num < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    binario = dec_binario(num)
    print(f"{num} en binario es: {binario}")

'''
#EJERCICIO 5
'''
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresa una palabra sin tildes ni espacios: ")

if texto.isalpha():
    if es_palindromo(texto):
        print(f"'{texto}' es palindromo.")
    else:
        print(f"'{texto}' no es un palindromo.")
else:
    print("Entrada invalida.")

'''
#EJERCICIO 6
'''
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

suma_digitos(1458)

'''
#EJERCICIO 7
'''
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
contar_bloques(5)

'''
#EJERCICIO 8
'''
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print(contar_digito(3433545456, 5))
'''