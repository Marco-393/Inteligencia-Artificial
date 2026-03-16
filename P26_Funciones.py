# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

# Datos para probar la función
lista_anios = [1900, 2000, 2016, 1987]
resultados_esperados = [False, True, True, False]

# Ejecutar pruebas
for i in range(len(lista_anios)):
    anio_actual = lista_anios[i]
    print(anio_actual, "-> ", end="")

    verificacion = es_bisiesto(anio_actual)

    if verificacion == resultados_esperados[i]:
        print("Correcto")
    else:
        print("Error")