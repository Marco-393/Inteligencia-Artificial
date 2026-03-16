# Función que determina si un año es bisiesto
def esAnioBisiesto(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# Función que devuelve la cantidad de días de un mes
def obtenerDiasMes(year, month):

    # Validar datos
    if year < 1582 or month < 1 or month > 12:
        return None

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Caso especial: febrero en año bisiesto
    if month == 2 and esAnioBisiesto(year):
        return 29

    return dias_mes[month - 1]


# Datos para probar la función
casos_prueba = [(1900,2),(2000,2),(2016,1),(1987,11)]
salidas_esperadas = [28,29,31,30]

# Ejecutar pruebas
for i in range(len(casos_prueba)):
    year, month = casos_prueba[i]
    print(year, month, "->", obtenerDiasMes(year, month))