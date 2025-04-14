"""
EJERCICIO 1
"""
# Definicion de la funcion
def imprimir_hola_mundo():
    print("Hola mundo!")

# Programa principal
imprimir_hola_mundo()

"""
EJERCICIO 2
"""
# Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_ingresado = input("Cual es tu nombre? ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)

"""
EJERCICIO 3
"""
# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingrese donde vive: ")

informacion_personal(nombre, apellido, edad, residencia)

"""
EJERCICIO 4
"""
# Definicion de funciones
def calcular_area_circulo(radio):
   return 3.14 * radio ** 2

def calcular_perimetro_circulo(radio):
   return 2 * 3.14 * radio

# Programa principal
radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: ", calcular_area_circulo(radio))
print(f"El perimetro del circulo es: ", calcular_perimetro_circulo(radio))

"""
EJERCICIO 5
"""
# Definicion de funciones
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = float(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")

"""
EJERCICIO 6
"""
# Definicion de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

"""
EJERCICIO 7
"""
# Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

"""
EJERCICIO 8
"""
# Definicion de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return (imc)

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc}")

"""
EJERCICIO 9
"""
# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return (fahrenheit)

# Programa principal
celsius = float(input("Ingrese los grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} °C en Fahrenheit son: {fahrenheit} °F")

"""
EJERCICIO 10
"""
# Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) /3
    return(promedio)

# Programa principal
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los numeros ingresados es: {promedio}")
