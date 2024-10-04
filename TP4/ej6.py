#Ejercicio 6: Crear y acceder a un diccionario.

def buscar_info(diccionario, clave):
    clave = clave.lower()
    return diccionario.get(clave, None)

diccionario = {
    "nombre": "Juan.",
    "edad": "30 años.",
    "ciudad": "Madrid."
}

while True:
    clave_a_buscar = input("¿Qué información deseas buscar? (nombre, edad, ciudad): ").lower()
    resultado = buscar_info(diccionario, clave_a_buscar)
    if resultado:
        print(f"- {clave_a_buscar.capitalize()}: {resultado}")
        break
    else:
        print("Clave no válida, por favor intenta nuevamente.")