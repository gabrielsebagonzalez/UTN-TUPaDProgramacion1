"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range(101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

num = int(input("Ingrese un número entero: "))
if num < 0:    #Si es negativo lo convierto a positivo
    num = -num 

if num == 0:
    digitos = 1
else:
    digitos = 0
    while num > 0:
        num //= 10  #Divido por 10 y queda la parte entera
        digitos += 1
print(f"La cantidad de digitos es {digitos}")


"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

suma = 0
valor_minimo = 0
valor_maximo = 0

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

if valor1 > valor2: #Si el valor1 es mayor los intercambio para que sea el menor 
    valor1, valor2 = valor2, valor1 

for i in range(valor1 + 1, valor2):
    suma += i

print(f"La suma de los números entre {valor1} y {valor2} es igual a {suma}")


"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

suma = 0

num = int(input("Ingrese un número entero (0 para finalizar): "))
while num != 0:
    suma += num
    num = int(input("Ingrese otro número entero (0 para finalizar): "))

print(f"El total acumulado es {suma}")


"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

print("****JUEGO DEL NÚMERO ALEATORIO****")
print("El juego consiste en adivinar un número secreto")
print()
num_aleatorio = random.randint(0,9)
intentos = 0
adivina = False

while adivina == False:
    num_usuario = int(input("Ingrese un número entre 0 y 9: "))

    while num_usuario < 0 or num_usuario > 9:
        num_usuario = int(input("Error! ingrese un número entre 0 y 9: "))
    intentos += 1

    if num_usuario == num_aleatorio:
        adivina = True
        print(f"Perfecto! el número secreto era {num_aleatorio}")
        print(f"Acertaste en {intentos} intentos!")


"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for par in range(100, 0, -2):
    print(par, end=" ")


"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

suma = 0

num = int(input("Ingrese un número entero positivo: "))
while num < 0:
    num = int(input("Error! debe ingresar un número entero positivo: "))

for i in range(num + 1):
    suma += i

print(f"La suma de los números comprendidos entre 0 y {num} es {suma}")


"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(100):
    num = int(input(f"Ingrese el numero entero {i + 1}: "))
    if num % 2 == 0: #El cero se considera par así que lo cuento
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:     #Hago un elif porque sino con el else cuenta al cero como negativo
        negativos += 1

print(f"La cantidad de números pares son: {pares}")
print(f"La cantidad de números impares son: {impares}")
print(f"La cantidad de números positivos son: {positivos}")
print(f"La cantidad de números negativos son: {negativos}")


"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

suma = 0
cant_numeros = 100 

for i in range(cant_numeros):
    num = int(input(f"Ingrese el número entero {i + 1}: "))
    suma += num
media = suma / cant_numeros #uso la variable para no poner i + 1

print(f"La suma de todos los valores ingresados es: {suma} y su media es: {media}")


"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""


num = int(input("Ingrese un número para invertir: "))
signo = -1 if num < 0 else 1  
num = abs(num)
num_invertido = 0

while num > 0:
    resto = num % 10
    num_invertido = num_invertido * 10 + resto
    num //= 10

num_invertido *= signo # Si el usuario ingresó un número negativo la variable signo será (-1)
print(f"El número invertido es {num_invertido}")
