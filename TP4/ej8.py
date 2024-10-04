#Ejercicio 8: Eliminar elementos de un diccionario.

mascota = {
    "especie" : "perro.",
    "nombre" : "Firulais.",    
    "edad" : "5 años."
}

mascota.pop("edad")

print("Diccionario luego de eliminar el elemento 'edad': ")
for clave, valor in mascota.items():
    print(f"- {clave.capitalize()}: {valor}")