"""1) Crear una lista con las notas de 10 estudiantes.
•Mostrar la lista completa.
•Calcular y mostrar el promedio.
•Indicar la nota más alta y la más baja."""

acum_notas = 0
notas_estudiantes = [7, 8, 9, 10, 6, 5, 8, 7, 9, 2]

for nota in notas_estudiantes:
    acum_notas += nota

promedio = acum_notas / len(notas_estudiantes)
min_nota = min(notas_estudiantes)
max_nota = max(notas_estudiantes)

print(f"Las notas de los estudiantes son: {notas_estudiantes}")
print(f"El promedio de las notas es: {promedio}")
print(f"La nota más alta es: {max_nota}")
print(f"La nota más baja es: {min_nota}")

"""2) Pedir al usuario que cargue 5 productos en una lista.
•Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
•Preguntar al usuario qué producto desea eliminar y actualizar la lista."""

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i + 1}: ")
    productos.append(producto)

lista_ordenada = sorted(productos, key=str.lower)
print(f"Lista ordenada alfabéticamente: {lista_ordenada}")

eliminar_producto = input("Desea eliminar algún producto? ingrese el nombre: ")

if eliminar_producto in productos:
    productos.remove(eliminar_producto)
    print("Producto eliminado correctamente")
else:
    print("El producto no se encuentra en el listado")

print(f"Lista actualizada: {productos}")

"""3) Generar una lista con 15 números enteros al azar entre 1 y 100.
•Crear una lista con los pares y otra con los impares.
•Mostrar cuántos números tiene cada lista."""

import random

lista_numeros = []
num_par = []
num_impar = []

for i in range(15):
    numero = random.randint(1, 100)
    lista_numeros.append(numero)

for num in lista_numeros:
    if num % 2 == 0:
        num_par.append(num)
    else:
        num_impar.append(num)


print(f"Lista de números aleatorios: {lista_numeros}")
print(f"Lista de números pares: {num_par} cantidad de números: {len(num_par)}")
print(f"Lista de números impares: {num_impar} cantidad de números: {len(num_impar)}")

"""4) Dada una lista con valores repetidos: datos = [1, 3, 5 , 3, 7, 1, 9, 5, 3]

•Crear una nueva lista sin elementos repetidos.
•Mostrar el resultado."""

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

nueva_lista = []

for dato in datos:
    if dato not in nueva_lista:
        nueva_lista.append(dato)

print(f"La lista original con valores repetidos es: {datos}")
print(f"La nueva lista sin valores repetidos es: {nueva_lista}")


"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
•Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
•Mostrar la lista final actualizada."""

estudiantes = ["Carlos", "Mauricio", "Sabrina", "Nestor", "Facundo", "Valentina", "María", "Fabiana"]
print(f"La lista de estudiantes original es: {estudiantes}")

opcion = input("Desea agregar un estudiante? presione(A) Eliminar? presione(E): ").upper()

while opcion != "A" and opcion != "E":
    opcion = input("Error! para agregar presione(A), Eliminar? presione(E): ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nuevo)
    print("Estudiante agregado exitosamente!")
else:
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ").upper()
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("Estudiante eliminado exitosamente!")
    else:
        print("El estudiante no se encuentra en la lista")

print(f"La lista actualizada es:")

"""6)
Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero)."""

numeros = [5, 10, 15, 40, 55, 2, 8]

numeros_rotados = [numeros [-1]] + numeros[:-1]

print(f"Lista de números original: {numeros}")
print(f"Los números rotados: {numeros_rotados} ")

"""7)
Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
•Calcular el promedio de las mínimas y el de las máximas.
•Mostrar en qué día se registró la mayor amplitud térmica."""

cont_minimas = 0
cont_maximas = 0
minima = 0
maxima = 0
amplitud = 0
mayor_amplitud = 0
dia = 0

temperaturas = [ 
    [8, 15], 
    [9, 16], 
    [7, 13], 
    [12, 18], 
    [15, 25], 
    [16, 26], 
    [18, 30]
    ]

for fila in temperaturas:
    cont_minimas += fila[0]

for fila in temperaturas:
    cont_maximas += fila[1]

prom_temp_min = cont_minimas / len(temperaturas)
prom_temp_max = cont_maximas / len(temperaturas)

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud = maxima - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia = i + 1

print(f"El promedio de temperaturas mínimas es: {round(prom_temp_min,2)}°")
print(f"El promedio de temperaturas máximas es: {round(prom_temp_max,2)}°")
print(f"El día con más amplitud térmica es el {dia} con {mayor_amplitud}°")


"""8)Crear una matriz con las notas de 5 estudiantes en 3 materias.
•Mostrar el promedio de cada estudiante.
•Mostrar el promedio de cada materia."""


notas = [
    [6, 7, 8], 
    [7, 7, 9], 
    [5, 8, 7], 
    [10, 9, 8], 
    [8, 8, 9]
    ]

print("****Promedio de cada estudiante****")
print()

for i in range(len(notas)):
    suma_notas = 0
    for j in range(len(notas[i])):
        suma_notas += notas[i][j]
    promedio = suma_notas / len(notas[i])
    print(f"Promedio del estudiante { i + 1} = {round(promedio, 2)}")

print()
print("****Promedio de cada materia****")
print()

for j in range(len(notas[0])):
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas += notas[i][j]
    promedio = suma_notas / len(notas)
    print(f"El promedio de cada materia es: {promedio}")


"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
•Inicializarlo con guiones "-" representando casillas vacías.
•Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
•Mostrar el tablero después de cada jugada."""

tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
    for celda in fila:
        print(celda, end=" ")
    print()

jugador = "X"
jugadas = 0
ganador = None

while jugadas < 9 and ganador is None:
    print(f"\nTurno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango, intente de nuevo")
        continue

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print("Casilla ocupada, intente de nuevo")
        continue

    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            ganador = tablero[i][0]

    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] != "-":
            ganador = tablero[0][j]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
        ganador = tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
        ganador = tablero[0][2]

    if ganador is not None:
        print(f"\nEl jugador {jugador} ganó!")
        break

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"


if ganador is None and jugadas == 9:
    print(f"\nEmpate, no hay ganador")

"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
•Mostrar el total vendido por cada producto.
•Mostrar el día con mayores ventas totales.
•Indicar cuál fue el producto más vendido en la semana."""

ventas = [
    [5, 8, 6, 7, 4, 3, 6],   
    [3, 6, 4, 5, 2, 7, 8],   
    [10, 12, 8, 9, 11, 15, 14],  
    [7, 5, 6, 8, 9, 10, 12]  
]

mayor_producto = 0
producto_mayor = 0


#Total vendido por cada producto
print("****Total vendido por cada producto****")
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    print(f"El total vendido del producto {i + 1} es {total_producto}")

    if total_producto > mayor_producto:
        mayor_producto = total_producto
        producto_mayor = i + 1

#Día con mayores ventas totales
print("****Total de ventas por día****")

dia = 0
may_ventas_totales = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    print(f"Total del día {j + 1} con {total_dia} ventas")
    if total_dia > may_ventas_totales:
        may_ventas_totales = total_dia
        dia = j + 1
print(f"El día {dia} tiene las mayores ventas con {may_ventas_totales}")

print("****producto más vendido en la semana****")
print(f"El producto más vendido de la semana fué el {producto_mayor} con {mayor_producto} ventas")