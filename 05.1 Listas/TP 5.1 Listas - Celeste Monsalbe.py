"""
EJERCICIO 1
"""
multiplos_4 = list(range(4, 100, 4))

print(multiplos_4)

"""
EJERCICIO 2
"""
lista_mascotas = ["perro", "gato", "conejo", "hamster", "tortuga"]

print(lista_mascotas[-2])

"""
EJERCICIO 3
"""
lista_vacia = []

lista_vacia.append("tenedor")
lista_vacia.append("plato")
lista_vacia.append("vaso")

print(lista_vacia)


"""
EJERCICIO 4
"""
animales = ["perro","gato","conejo","pez"]

animales[1]="loro"
animales[-1]="oso"
print(animales)

"""
EJERCICIO 5
"""
#El programa lo que hace es usar la funcion remove para eliminar el numero mas grande de la lista usando max, que en este caso seria el 22. La lista actualizada seria:
[8,15,3,7]

"""
EJERCICIO 6
"""
lista_numeros = list(range(10, 31, 5))

print(lista_numeros)

"""
EJERCICIO 7
"""
autos=["sedan","polo","suran","gol"]

autos[1] = "fox"
autos[2] = "voyage"
print(autos)

"""
EJERCICIO 8
"""
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

"""
EJERCICIO 9
"""
# Lista de compras de diferentes clientes
compras = [
    ["pan", "leche"], 
    ["arroz", "fideos", "salsa"], 
    ["agua"]
]
compras[2].append("jugo") # Se agrega la palabra "jugo" a la lista 3
compras[1][compras[1].index("fideos")] = "tallarines" # Se reemplaza la palabra "fideos" por "tallarines"
compras[0].remove("pan") # Se elimina la palabra "pan" de la lista 1
print(compras)

"""
EJERCICIO 10
"""
lista_anidada = [
    [15],
    [True],
    [25.5, 57.9, 30.6],
    [False]
]
print(lista_anidada)