# Definición de la función  con def nombre de la función y los dos parámetros
def calcular_descuento(monto_total, porcentaje_descuento):
    descuento = monto_total * (porcentaje_descuento / 100)    # valor código
    return descuento       # valor retorno

# Entrada de datos que se solicita al usuario

monto_total = float(input("Ingrese el valor del total $:  "))  # ingreso del valor total
porcentaje_descuento = float(input("Ingrese el porcentaje del descuento %: ")) # ingreso del porsentaje
                                                                               # de descuento
# Primera llamada: con el porcentaje ingresado por el usuario
descuento1 = calcular_descuento(monto_total, porcentaje_descuento)
monto_final1 = monto_total - descuento1

print("\n=== PRIMERA COMPRA ===")
print(f"El monto total es: $ {monto_total}")
print(f"El porcentaje de descuento es: {porcentaje_descuento}%")
print(f"Descuento aplicado:$ {descuento1}")
print(f"Monto final a pagar:$ {monto_final1}")

# Segunda llamada: aplicando un 20% fijo
descuento2 = calcular_descuento(monto_total, 20)
monto_final2 = monto_total - descuento2

print("\n=== SEGUNDA COMPRA (20% de descuento) ===")
print(f"El monto total es:$ {monto_total}")
print("El porcentaje de descuento es: 20%")
print(f"Descuento aplicado:$ {descuento2}")
print(f"Monto final a pagar:$ {monto_final2}")
