#Ejercicio 10: Diccionario anidado.

alumnos = { 
    "alumno1": {"nombre": "Carlos", "edad": 20, "nota": 8.5}, 
    "alumno2": {"nombre": "Lucía", "edad": 22, "nota": 9.0}, 
    "alumno3": {"nombre": "Ana", "edad": 21, "nota": 7.5}
}

print(f"Nombre del alumno2: {alumnos['alumno2']['nombre']}.")
print()
print(f"Nota del alumno3: {alumnos['alumno3']['nota']}")