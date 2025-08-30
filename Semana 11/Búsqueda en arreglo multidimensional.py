# Programa de búsqueda en arreglo multidimensional

# Matriz bidimensional 3x3
matriz = [
    [24, 17, 11],
    [29, 12, 16],
    [35, 33, 28]
]
# Función para buscar un valor especifico en la matriz
# Determinar el valor a buscar

valor_buscado = 12

if any(valor_buscado in fila for fila in matriz  ):
    print(f"✅ {valor_buscado} se encontró en la matriz.")
else:
    print(f"❌{valor_buscado} no se encontró en la matriz.")

# Mostrar la posición de valor en la matriz si se encontró.
# Variable de control

posiciones = []

# Recorremos la matriz
for i in range(len(matriz)):          # filas
    for j in range(len(matriz[i])):   # columnas
        if matriz[i][j] == valor_buscado:
            posiciones.append((i, j))  # guardamos la posición encontrada

# Mostrar posición
if posiciones:
    print(f"En las posiciones:")
    for fila, col in posiciones:
        print(f"   Fila {fila}, Columna {col}")




