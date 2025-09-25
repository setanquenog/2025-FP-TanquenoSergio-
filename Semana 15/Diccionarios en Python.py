# Crear un Diccionario
informacion_personal = {
    "Nombre": "Sergio Tanqueño",
    "Edad": "45 años",
    "Ciudad": "Ambato",
    "Profesion": "Estudiante"
}
# imprimir diccionario inicial
print("")
print("DICCIONARIO INICIAL")
print("====================")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Acceder y Modificar Valores
informacion_personal["Ciudad"] = "Puyo"

# Agregar/actualizar la profesión
informacion_personal["Profesion"] = "Bachiller Técnico Industrial"

# Verificar Existencia de Claves
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0989352929"

# Eliminar la clave "edad"
del informacion_personal["Edad"]

# Imprimir en columnas (cada clave en una fila)
print("")
print("DICCIONARIO FINAL")
print("====================")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
