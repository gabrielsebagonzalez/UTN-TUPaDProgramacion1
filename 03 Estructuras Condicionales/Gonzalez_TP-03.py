"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

MAYOR_DE_EDAD = 18
edad_usuario = int(input("Ingrese su edad por favor: "))

if edad_usuario > MAYOR_DE_EDAD:
    print("Es mayor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”."""

nota = float(input("Ingrese la nota del usuario: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero = int(input("Ingrese un número para saber su paridad: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

edad_usuario = int(input("Ingrese su edad por favor: "))

#utilizo sólo los límites superiores en los operadores relacionales
if edad_usuario < 0:
    print("Ud ingresó una edad inválida")
elif edad_usuario < 12:
    print("Es un niño")
elif edad_usuario < 18:
    print("Es un adolescente")
elif edad_usuario < 30:
    print("Es un joven")
else:
    print("Es un adulto")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string."""

password = len(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

if password >= 8 and password <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: from statistics import mode, median, mean mi_lista = [1,2,5,5,3] mean(mi_lista) En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria."""

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Los valores no cumplen con ninguno de los criterios de sesgo")

print(f"media = {media}\nmediana = {mediana}\nmoda = {moda}")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[-1].lower()

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(frase)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

nombre = input("Ingrese su nombre por favor: ")
print("*****MENÚ DE OPCIONES*****")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Elija un número del 1 al 3 de acuerdo a la opción deseada: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingresó una opción inválida")

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud = float(input("Ingrese la magnitud del terremoto: "))

#Solamente verifico los límites superiores de los operadores relacionales.
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
Periodo del año                Hemisferio Norte   Hemisferio Sur
21 Dic - 20 Mar (incl.)        Invierno           Verano
21 Mar - 20 Jun (incl.)        Primavera          Otoño
21 Jun - 20 Sep (incl.)        Verano             Invierno
21 Sep - 20 Dic (incl.)        Otoño              Primavera
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("Ingrese la letra de acuerdo al hemisferio en que se encuentra (Norte = N / Sur = S): ").upper()
#Tengo una extensión de VSCode que cambia el simbolo de desigualdad
if hemisferio != "N" and hemisferio != "S": 
    print("Error!, debe ingresar N o S")
    exit()

mes = int(input("Ingrese el mes del 1 al 12: "))
if mes < 1 or mes > 12:
    print("Error!, debe ingresar un mes entre 1 y 12")
    exit()

dia = int(input("Ingrese el día del 1 al 31: "))
if dia < 1 or dia > 31:
    print("Error!, debe ingresar días entre 1 y 31")
    exit()

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >=21) or (4 <= mes and mes <= 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif(mes == 6 and dia >= 21) or (7 <= mes and mes <= 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print(f"La estación del año es {estacion}")