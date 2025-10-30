"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""

print("1. Archivo inicial con productos")
with open("productos.txt", "w") as archivo:
    archivo.write("aceite,2500,50\n")
    archivo.write("azucar, 900,100\n")
    archivo.write("harina,1300,45\n")
print("Archivo productos.txt creado correctamente")


"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""

print("2. Leer y mostrar productos")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente."""

print("3. Agregar productos")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    
print("*****Agregar un nuevo producto*****")
nombre =  input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado exitosamente")


"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad."""

print("4. Cargar productos en una lista de diccionarios")

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre,precio,cantidad = linea.split(",")

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        productos.append(producto)

for producto in productos:
    print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")

print("\nLista cargada correctamente")


"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error."""

print("5. Buscar productos por nombre")

buscar_producto = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscar_producto.lower():
        print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")
        encontrado = True
        break

if not encontrado:
    print("El producto no se encuentra en el listado")


"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista."""

print("6. Guardar los productos actualizados")

with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("Archivo actualizado correctamente")