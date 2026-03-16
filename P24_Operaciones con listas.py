# Lista inicial con números repetidos
numeros = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Lista donde se guardarán solo los valores únicos
sin_repetidos = []

# Recorrer cada número de la lista original
for valor in numeros:
    if valor not in sin_repetidos:
        sin_repetidos.append(valor)

# Reemplazar la lista original con la lista filtrada
numeros = sin_repetidos

# Mostrar resultado
print("Lista sin elementos repetidos:")
print(numeros)