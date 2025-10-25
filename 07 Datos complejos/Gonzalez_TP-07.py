"""1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios."""

precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

frutas = list(precios_frutas.keys())
print(frutas)


"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto número {i+1} por favor: ")
    telefono = int(input("Ingrese su número telefónico: "))
    contactos[nombre] = telefono

print("Se cargaron los 5 contactos exitosamente")

buscar_nombre = input("Ingrese el nombre del contacto a buscar: ")
if buscar_nombre in contactos:
    print(f"El número telefónico de {buscar_nombre} es: {contactos[buscar_nombre]}")
else:
    print("El usuario no existe en nuestra base de datos")


"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

cant_palabra = {}

for palabra in palabras:
    if palabra in cant_palabra:
        cant_palabra[palabra] += 1
    else:
        cant_palabra[palabra] = 1

print(f"Cantidad de veces que aparece cada palabra: {cant_palabra}")


"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo:"""

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")

    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} del alumno {nombre}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El alumno {nombre} tiene un promedio de {promedio:.2f}")


"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

parcial1 = {"Juan", "María", "Pedro", "Ana"}
parcial2 = {"Pedro", "Lucía", "Ana", "Carlos"}

aprobaron_ambos = parcial1 & parcial2
print(f"Aprobaron ambos parciales: {aprobaron_ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Aprobaron solo uno: {solo_uno}")

al_menos_uno = parcial1 | parcial2
print(f"Aprobó al menos un parcial: {al_menos_uno}")


"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""


"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
Permití consultar qué actividad hay en cierto día y hora."""

agenda = {}

print("*****Agenda de activides*****")

agregar = "s"
while agregar == "s":
    dia = input("Ingrese el día: ").strip().lower()
    hora = input("Ingrese la hora en formato HH:MM: ").strip()
    actividad = input("Ingrese la actividad: ").strip()

    clave = (dia, hora)
    agenda[clave] = actividad

    agregar = input("¿Desea agregar otra actividad? (s/n): ").strip().lower()

print("\n*****Consulta de agenda*****")

dia_consulta = input("Ingrese el día a consultar: ").strip().lower()
hora_consulta = input("Ingrese la hora (HH:MM): ").strip()

clave_consulta = (dia_consulta, hora_consulta)

if clave_consulta in agenda:
    print(f"Actividad: {agenda[clave_consulta]}")
else:
    print("No hay actividad programada en esa fecha")


"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. Ejemplo:

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
"""

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"Original: {paises_capitales}")
print(f"Invertido: {capitales_paises}")