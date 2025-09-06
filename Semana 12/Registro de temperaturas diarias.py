# Matriz en 3D del registro de temperatura diaria en ciudades

# Ciudades, semanas y dias

ciudades = ["Puyo", "Ambato", "Quito"]
semanas = 3
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D con sus valores
# Temperatura [ciudad] [semana] [dias]

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

#Mostrar temperatura en ciudad, semana y día específicos

ciudad_idx = 0   # 0 = Puyo, 1 = Ambato, 2 = Quito
semana_idx = 1   # 0 = Semana 1, 1 = Semana 2, 2 = Semana 3
dia_idx = 4      # 0 = Lunes, 1 = Martes, ..., 6 = Domingo

print(f"Temperatura en {ciudades[ciudad_idx]}, semana {semana_idx+1}, día {dias[dia_idx]}: {temperaturas[ciudad_idx][semana_idx][dia_idx]} °C\n")


#Calcular promedio de temperaturas por ciudad y semana

for i in range(len(ciudades)):  # recorrer ciudades
    print(f"Ciudad: {ciudades[i]}")
    for j in range(len(temperaturas[i])):  # recorrer semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # recorrer días
            suma += temperaturas[i][j][k]
        promedio = suma / len(temperaturas[i][j])
        print(f"  Semana {j+1}: promedio = {promedio:.2f} °C")
    print()