"""
EJERCICIO 1
"""
#Se le pregunta la edad al usuario
edad = int(input("Cual es tu edad?"))

#Se comprueba si el usuario es mayor de edad o no
if (edad >= 18):
    print("Es mayor de edad")


"""
EJERCICIO 2
"""
#Se solicita la nota al usuario
nota = int(input("Ingrese su nota: "))

#Se determina si el usuario aprobo o desaprobo
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")


"""
EJERCICIO 3
"""
#Se le pide al usuario que ingrese un numero par
num_par = int(input("Ingrese un numero par: "))

#Se verifica si el numero es par
if num_par % 2 == 0:
    print("Usted ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")


"""
EJERCICIO 4
"""
#Se le pide la edad al usuario
edad = int(input("Ingrese su edad: "))

#Se determina a que categoria pertenece segun su edad
if edad < 12:
    print("Sos un niño/a")
elif (edad >= 12) and (edad < 18):
    print("Sos un adolescente")
elif (edad >= 18) and (edad < 30):
    print("Sos un adulto/a joven")
else:
    print("Sos un/a adulto/a") 


""" 
EJERCICIO 5
"""
#Se le pide al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña: ")

#Se determina si el usuario cumplio con las condiciones de la contraseña o no
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


"""
EJERCICIO 6
"""
#Se importan las herramientas necesarias para el programa
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Se calculan las estadisticas
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Se imprimen los valores
print(f"Media: {media}\nMediana: {mediana}\nModa: {moda}")

#Se determinan los sesgos
if media > mediana and mediana > moda:
    print("El sesgo es positivo")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo")
else:
    print("No hay sesgo")



"""
EJERCICIO 7
"""
#Se le pide al usuario que ingrese una palabra o frase
palabra = input("Ingrese una palabra o frase: ")

#Se imprime el resultado final de la frase o palabra que ingreso el usuario
if palabra and palabra[-1] in "aeiou":
    print(f"{palabra}!")
else:
    print(f"{palabra}")



"""
EJERCICIO 8
"""
#Se le piden los datos al usuario
usuario_nom = input(f"Ingrese su nombre: " )
usuario_num = input("Elija un numero del 1 al 3 teniendo en cuenta las siguientes opciones: \n"
                    "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n"
                    "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n"
                    "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

#Se imprime el resultado final segun los datos que ingreso el usuario
if usuario_num == 1:
    print(usuario_nom.upper())
elif usuario_num == 2:
    print(usuario_nom.lower())
else:
    print(usuario_nom.title())



"""
EJERCICIO 9
"""
#Se le pide la magnitud del terremoto al usuario
mag_terremoto = int(input("Ingrese la magnitud del terremoto: "))

#Clasificacion de la magnitud ingresada
if mag_terremoto < 3:                          #Si la magnitud es menor a 3 
    print("Muy leve (imperceptible)")
elif mag_terremoto >= 3 and mag_terremoto < 4: #Si la magnitud esta entre 3 y 4
    print("Leve (ligeramente perceptible)")
elif mag_terremoto >= 4 and mag_terremoto < 5: #Si la magnitud esta entre 4 y 5 
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif mag_terremoto >= 5 and mag_terremoto < 6: #Si la magnitud esta entre 5 y 6
    print("Fuerte (puede causar daños en estructuras debiles)") 
elif mag_terremoto >= 6 and mag_terremoto < 7: #Si la magnitud esta entre 6 y 7
    print("Muy fuerte (puede causar daños significativos)")
else:                                          #Si la magnitud es mayor o igual a 7
    print("Extremo (puede causar graves daños a gran escala)")



"""
EJERCICIO 10
"""
# Solicitar al usuario que ingrese la información
hemisferio = input("¿En qué hemisferio te encontras (N/S)? ")
mes = int(input("¿Qué mes del año es (1-12)? "))
dia = int(input("¿Qué día es? "))

#Se define la estacion en base a los datos proporcionados
if hemisferio == "N":
    if mes == 3 and dia >= 20 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
      print("Estas en primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
      print("Estas en verano")
    elif mes == 9 and dia >= 23 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
      print("Estas en otoño")
    else:
      print("Estas en invierno")
elif hemisferio == "S":
    if mes == 3 and dia >= 20 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
      print("Estas en otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
      print("Estas en invierno")
    elif mes == 9 and dia >= 23 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
      print("Estas en primavera")
    else:
      print("Estas en verano")
else:
  print("Datos incorrectos")