"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

name = input("Ingrese su nombre: ")
saludar = saludar_usuario(name)
print(saludar)

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nom_usuario = input("Ingrese su nombre: ")
ape_usuario = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_res = input("Ingrese su lugar de residencia: ")

informacion_personal(nom_usuario, ape_usuario, edad, lugar_res)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""

import math

def calcular_area_circulo(radio):
    return math.pi * pow(radio, 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el valor del radio: "))

area_circulo = calcular_area_circulo(radio)
perimetro_circulo = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {round(area_circulo, 2)}")
print(f"El perímetro del círculo es: {round(perimetro_circulo, 2)}")


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""

SEGUNDOS_POR_HORA = 3600

def segundos_a_horas(segundos):
    return segundos / SEGUNDOS_POR_HORA

segundos = int(input("Ingrese los segundos para convertir a horas: "))
horas = segundos_a_horas(segundos)
print(f"Los {segundos} segundos equivalen a {horas:.2f} horas")


"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla = int(input("Ingrese el número de la tabla de multiplicar: "))
tabla_multiplicar(tabla)


"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return(suma, resta, multiplicacion, division)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

operacion = operaciones_basicas(num1, num2)

print(f"La suma de los números es: {operacion[0]}")
print(f"La resta de los números es: {operacion[1]}")
print(f"La multiplicación de los números es: {operacion[2]}")
print(f"La división de los números es: {operacion[3]}")


"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    return peso / pow(altura,2)

peso_usuario = float(input("Ingrese su peso por favor: "))
altura_usuario = float(input("Ingrese su altura por favor: "))

imc = calcular_imc(peso_usuario, altura_usuario)
print(f"Su índice de masa corporal es: {imc:.2f}")


"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp = float(input("Ingrese los grados Celsius a transformar: "))
temp_equivalente = celsius_a_fahrenheit(temp)

print(f"Los {temp}° Celsius equivalen a {temp_equivalente} Fahrenheit")


"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

num_promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los números {num1}, {num2} y {num3} = {num_promedio}")
