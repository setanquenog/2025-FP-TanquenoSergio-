# Programa de ordenación en arreglo multidimensional

# Matriz bidimensional 3x3
matriz = [
    [24, 17, 11],
    [29, 12, 16],
    [35, 33, 28]
]

# Función Bubble Sort para ordenar una lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:  # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        bubble_sort(matriz[fila])
        return True
    else:
        return False

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario digite el número de fila a ordenar
fila_usuario = int(input("\nDigite fila a ordenar (0, 1 o 2): "))

if ordenar_fila(matriz, fila_usuario):
    print(f"\n✅ La fila {fila_usuario} fue ordenada en orden ascendente.")
else:
    print("\n❌ Fila fuera de rango. Intente con 0, 1 o 2.")

# Mostrar matriz modificada con su fila elegida ordenada
print("\nMatriz después de ordenar:")
for fila in matriz:
    print(fila)