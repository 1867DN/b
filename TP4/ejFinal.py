#Ejercicio Final 
#Sistema de Gestión de Inventario de Tienda 

inventario = {
    "A001" : ("Monitor LG", 260),
    "A002" : ("Teclado Razer", 50),
    "A003" : ("Auricular Hyperx", 30),
    "A004" : ("Procesador Ryzen 7", 420),
    "A005" : ("Mouse Logitech", 90),
    "A006" : ("IPhone X", 380),
    "A007" : ("Cable USB C", 15)
}

#mostrar_inventario(inventario): Muestra todos los productos del 
#inventario con su código, descripción y precio. 
def mostrar_inventario(inventario):
    for codigo, (descripcion, precio) in inventario.items():
        print(f"- Código : {codigo}, Descripción : {descripcion}, Precio : ${precio}.")

#buscar_producto(inventario, codigo): Busca un producto por su código. 
#Si existe, muestra su descripción y precio.
def buscar_producto(inventario):
    codigo = input("Ingresá el código del producto a buscar: ").upper()
    if codigo in inventario:
        descripcion, precio = inventario[codigo]
        print(f"- Producto encontrado: {descripcion}, Precio: ${precio}.")
    else:
        print(f"El producto con código {codigo} no fue encontrado.")

#modificar_precio(inventario, codigo, nuevo_precio): Modifica el precio 
#de un producto dado su código. 
def modificar_precio(inventario):
    codigo = input("Ingresá el código del producto a modificar: ").upper()
    if codigo in inventario:
        while True:
            try:
                nuevo_precio = float(input("Ingresá el nuevo precio: $"))
                break
            except ValueError:
                print("Ingresá un valor válido.")
        descripcion, _ = inventario[codigo]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"- El precio del producto con código '{codigo}' ha sido actualizado a: '${nuevo_precio}'.")
    else:
        print(f"El producto con código '{codigo}' no fue encontrado.")

#eliminar_producto(inventario, codigo): Elimina un producto del 
#inventario usando su código.
def eliminar_producto(inventario):
    codigo = input("Ingresá el código del producto a eliminar: ").upper()
    try:
        producto = inventario.pop(codigo)
        print(f"El producto con código '{codigo}' ha sido eliminado del inventario.")
    except KeyError:
        print(f"El producto con código '{codigo}' no fue encontrado.")

#productos_por_rango_de_precio(inventario, min_precio, max_precio): 
#Muestra todos los productos cuyo precio esté entre min_precio y 
#max_precio. 
def productos_por_rango_de_precio(inventario):
    while True:
        try:
            min_precio = float(input("Ingrese el precio mínimo: $"))
            max_precio = float(input("Ingrese el precio máximo: $"))
            if min_precio > max_precio:
                print("El mínimo no puede ser mayor al máximo.")
                continue
            break
        except ValueError:
            print("Ingresá un valor válido.")
    
    encontrado = False
    for codigo, (descripcion, precio) in inventario.items():
        if min_precio <= precio <= max_precio:
            if not encontrado:
                print(f"\nProductos en el rango de precio entre '${min_precio}' y '${max_precio}':")
                encontrado = True
            print(f"- Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}.")

    if not encontrado:
        print("\n- No hay valores en ese rango.")

#menu principal
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Mostrar Inventario")
        print("2. Buscar Producto")
        print("3. Modificar Precio")
        print("4. Eliminar Producto")
        print("5. Productos por Rango de Precio")
        print("6. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            buscar_producto(inventario)
        elif opcion == "3":
            modificar_precio(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            productos_por_rango_de_precio(inventario)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()