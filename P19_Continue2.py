# Solicitar una palabra y convertirla a mayúsculas
palabra = input("Introduce una palabra: ").upper()
salida = ""

# Recorrer cada letra
for letra in palabra:
    # Ignorar las vocales
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        salida = salida + letra

# Mostrar la palabra sin vocales
print(salida)