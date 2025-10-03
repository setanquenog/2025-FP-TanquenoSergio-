# Escritura y lectura de archivos de texto en Python

# --- Escritura en el archivo ---
# Abrimos el archivo en modo escritura ("w").
# Si no existe, lo crea. Si ya existe reemplaza su contenido.
with open("my_notes.txt", "w") as file:
    # Escribimos tres notas de líneas personales file.write
    file.write("Nota 1: Soy estudiante de la Universidad Estatal Amazónica.\n")
    file.write("Nota 2: Sigo la carrera de Tecnologías de la Información.\n")
    file.write("Nota 3: Modalidad de estudios en línea.\n")

# --- Lectura del archivo ---
# Abrimos el archivo en modo lectura ("r")
file = open("my_notes.txt", "r")

# Leemos línea por línea utilizando readline()
print("Contenido del archivo:")
linea = file.readline()
while linea:  # mientras exista una línea
    print(linea.strip())  # mostramos la línea sin saltos de línea extra
    linea = file.readline()  # leemos la siguiente línea

# Cerramos el archivo después de la lectura
file.close()