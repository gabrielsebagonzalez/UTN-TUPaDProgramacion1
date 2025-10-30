"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    

num = int(input("Ingrese un número entero positivo: "))

print(f"Factoriales del 1 al {num}")

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    
num = int(input("Ingrese la cantidad de posisciones de la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {num}")

for i in range(num):
    print(f"Posición {i}: {fibonacci(i)}")

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general."""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
def main():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es igual a {resultado}")

main()


"""4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"."""

def decimal_a_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("Debe ingresar un número entero positivo")
    else:
        binario = decimal_a_binario(numero)
        print(f"El número {numero} en binario es {binario}")

main()


"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    
    else:
        return False
    
def main():
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")

main()


"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)"""


def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + suma_digitos(num // 10)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("Debe ingresar un número entero positivo")
    else:
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es {resultado}")

main()


"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)"""

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)
    
def main():
    numero = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
    if numero < 1:
        print("Debe ingresar un número entero positivo")
    else:
        total = contar_bloques(numero)
        print(f"Para construir la pirámide con base {numero} bloques, se necesitan {total} bloques")

main()


"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0"""

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))

    if numero < 0 or digito < 0 or digito > 9:
        print("Debe ingresar un número y dígitos válidos.")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
    
main()