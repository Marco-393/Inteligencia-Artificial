# Solicitar ingreso anual al usuario
ingreso = float(input("Ingresa tu ingreso anual: "))

# Calcular impuesto según el rango
if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02

# Evitar valores negativos
if impuesto < 0:
    impuesto = 0.0

# Redondear el resultado
impuesto = round(impuesto, 0)

# Mostrar el impuesto calculado
print("Impuesto a pagar:", impuesto, "pesos")