'''
EJERCICIO 1
'''
precios_frutas = {
    'Banana': 1200, 
    'Anana': 2500, 
    'Melon': 3000, 
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
'''
EJERCICIO 2
'''
precios_frutas = {
    'Banana': 1200, 
    'Anana': 2500, 
    'Melon': 3000, 
    'Uva': 1450, 
    'Naranja': 1200, 
    'Manzana': 1500, 
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)
'''
EJERCICIO 3
'''
precios_frutas = {
    'Banana': 1330,
    'Anana': 2500,
    'Melon': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)
'''
EJERCICIO 4
'''
agenda = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el numero telefonico de {nombre}: ")
    agenda[nombre] = numero

mostrar_nombre = input("\nIngresa el nombre del contacto que queres buscar: ")

if mostrar_nombre in agenda:
    print(f"El numero de {mostrar_nombre} es: {agenda[mostrar_nombre]}")
else:
    print(f"{mostrar_nombre} no esta en la agenda.")
'''
EJERCICIO 5
'''
frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print(palabras_unicas)
print(frecuencia_palabras)
'''
EJERCICIO 6
'''
alumnos = {}

for i in range():
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    print(f"Ingrese las 3 notas de {nombre}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas

print("Promedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")
'''
EJERCICIO 7
'''
parcial1 = {5, 7, 8, 9}
parcial2 = {3, 6, 7, 8}

ambos_parciales = parcial1 & parcial2
print("Apobaron ambos parciales:", ambos_parciales)

un_parcial = parcial1 ^ parcial2
print("Aprobaron solo un parcial:", un_parcial)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", al_menos_uno)
'''
EJERCICIO 8
'''
stock_productos = {
    "leche": 8,
    "yerba": 5,
    "fideos": 10,
    "gaseosa": 7
}

while True:
    print("Opciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")

    opcion = input("Elegi una opcion (1-4): ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no esta en el sistema.")

    elif opcion == "2":
        producto = input("Ingresa el nombre del producto: ")
        if producto in stock_productos:
            try:
                cantidad = int(input("Cuantas unidades queres agregar?: "))
                stock_productos[producto] += cantidad
                print(f"Stock actualizado: {producto} ahora tiene {stock_productos[producto]}")
            except ValueError:
                print("Por favor, ingresa un numero valido")
        else:
            print(f"El producto '{producto}' no existe")

    elif opcion == "3":
        producto = input("Ingresa el nuevo producto: ")
        if producto in stock_productos:
            print(f"El producto '{producto}' ya existe")
        else:
            try:
                cantidad = int(input("Cuantas unidades queres agregar?"))
                stock_productos[producto] = cantidad
                print(f"Producto '{producto}' agregado con {cantidad} unidades")
            except ValueError:
                print("Por favor, ingresa un numero valido")
    
    else:
        print("Saliendo del sistema...")
    break
'''
EJERCICIO 9 
'''
agenda = {
    ("lunes", "10:00"): "Reunion con equipo",
    ("martes", "14:00"): "Clase de ingles",
    ("miércoles", "09:00"): "Entrenamiento",
    ("viernes", "16:00"): "Entrega de informe"
}

def consultar_evento():
    dia = input("Ingresa el dia: ")
    hora = input("Ingresa la hora (formato HH:MM): ")

    clave = (dia, hora)
    if clave in agenda:
        print(f"Actividad programada: {agenda[clave]}")
    else:
        print("No hay actividad registrada en ese día y hora.")

while True:
    print("Consulta de agenda")
    consultar_evento()
    salir = input("Queres consultar otra actividad? (s/n): ")
    if salir != 's':
        print("Fin de la consulta")
        break
'''
EJERCICIO 10
'''
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "Paris",
    "Italia": "Roma",
    "Japon": "Tokio",
    "Brasil": "Brasilia"
}

capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

print("Diccionario invertido (capital -> país):")
for capital, pais in capitales_a_paises.items():
    print(f"{capital}: {pais}")