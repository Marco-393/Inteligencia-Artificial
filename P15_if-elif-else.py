# Pedir el año al usuario
year = int(input("Escribe un año: "))

# Verificar si está dentro del calendario gregoriano
if year < 1582:
    print("Año fuera del calendario gregoriano")
else:
    # Comprobar si el año es bisiesto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Es un año bisiesto")
    else:
        print("Es un año común")