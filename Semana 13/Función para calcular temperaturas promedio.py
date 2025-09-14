# Desarrollo de Función para Calcular Temperaturas Promedio

def promedio_ciudad_y_semanas(temperaturas, ciudades):
    """
    Calcula el promedio total y semanal de temperaturas por ciudad.

    Parámetros:
        temperaturas (list): matriz 3D [ciudad][semana][día]
        ciudades (list): lista con nombres de las ciudades

    Retorna:
        dict: diccionario con promedio total y promedio por semana de cada ciudad
    """
    resultados = {}

    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        contador_total = 0
        promedios_semanales = []

        for semana in temperaturas[i]:
            suma_semana = sum(semana)
            promedio_semana = suma_semana / len(semana)
            promedios_semanales.append(promedio_semana)

            suma_total += suma_semana
            contador_total += len(semana)

        promedio_total = suma_total / contador_total
        resultados[ciudad] = {
            "Promedio total": promedio_total,
            "Promedios por semana": promedios_semanales
        }

    return resultados


# Matriz 3D con sus valores
# Temperatura [ciudad] [semana] [dias]

ciudades = ["Puyo", "Ambato", "Quito"]

temperaturas = [
    [ # Puyo
        [18,16,17,15,19,20,21], #semana 1
        [25,23,24,22,26,27,28], #semana 2
        [24,30,27,28,22,26,31]  #semana 3
    ],
    [ # Ambato
        [20,16,17,18,19,15,21], #semana 1
        [26,23,24,25,22,27,28], #semana 2
        [27,30,25,28,22,26,31]  #semana 3
    ],
    [ # Quito
        [15,16,17,18,19,20,21], #semana 1
        [22,23,24,25,26,27,28], #semana 2
        [23,22,24,25,26,29,30]  #semana 3
    ]
]

resultado = promedio_ciudad_y_semanas(temperaturas, ciudades)

# Mostrar resultados temperatura promedio por ciudad
# Temperatura promedio por semana
for ciudad, datos in resultado.items():
    print(f"\nCiudad: {ciudad}, promedio total: {datos ['Promedio total']:.2f} °C")
    for i, prom_semana in enumerate(datos["Promedios por semana"], start=1):
        print(f"  Semana {i}: {prom_semana:.2f} °C")

