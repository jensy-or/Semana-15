# -------- DICCIONARIOS --------
# Crear un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Jensy Ordonez",      # Nombre de la persona
    "edad": 31,                  # Edad de la persona
    "ciudad": "Cuenca",          # Ciudad donde vive la persona
    "profesion": "Ingeniera"     # Profesión de la persona
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"  # Cambiar la ciudad a Barcelona

# Agregar una nueva clave-valor al diccionario para representar la "profesion"
informacion_personal["profesion"] = "Ingeniero Ambiental"  # Actualizar la profesión

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:  # Si la clave "telefono" no existe
    informacion_personal["telefono"] = "985061138"  # Agregar un número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:  # Si la clave "edad" existe
    del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)  # Mostrar el diccionario final
