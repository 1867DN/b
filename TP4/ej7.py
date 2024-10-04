#Ejercicio 7: Modificar un diccionario.

persona = {
    "nombre": "Juan.",
    "edad": "30 años.",
    "ciudad": "Madrid."
}

print("El diccionario antiguo era:")
for clave, valor in persona.items():
    print(f"- {clave.capitalize()}: {valor}")
print()

persona["edad"] = "31 años."
persona["profesión"] = "Ingeniero."

print("El diccionario nuevo es: ")
for clave, valor in persona.items():
    print(f"- {clave.capitalize()}: {valor}")