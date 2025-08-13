#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro."""

import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area} y su perímetro es: {perimetro}")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale."""

segundos = int(input("Ingrese los segundos para convertir a horas por favor: "))
horas = segundos / 3600

print(f"Los {segundos} segundos equivalen a {horas} horas")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número."""

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"""
{numero} x 0  = {numero * 0}
{numero} x 1  = {numero * 1}
{numero} x 2  = {numero * 2}
{numero} x 3  = {numero * 3}
{numero} x 4  = {numero * 4}
{numero} x 5  = {numero * 5}
{numero} x 6  = {numero * 6}
{numero} x 7  = {numero * 7}
{numero} x 8  = {numero * 8}
{numero} x 9  = {numero * 9}
{numero} x 10 = {numero * 10}
""")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

num1 = int(input("Ingrese el primer número distinto de cero: "))
num2 = int(input("Ingrese el segundo número distinto de cero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma entre el número {num1} y {num2} es: {suma}")
print(f"La resta entre el número {num1} y {num2} es: {resta}")
print(f"La multiplicación entre el número {num1} y {num2} es: {multiplicacion}")
print(f"La división entre el número {num1} y {num2} es: {division}")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2"""

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / altura ** 2

print(f"Su índice de masa corporal es igual a: {imc}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32"""

grados_celsius = float(input("Ingrese la temperatura para transformar a grados Fahrenheit: "))

grados_fahrenheit = 9/5 * grados_celsius + 32

print(f"Los {grados_celsius} grados Celsius equivalen a {grados_fahrenheit} grados Fahrenheit")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números."""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3
promedio = suma / 3

print(f"El promedio de números ingresados es: {promedio}")