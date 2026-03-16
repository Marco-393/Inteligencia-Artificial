# Pedir una palabra al usuario y convertirla a mayúsculas
palabra_usuario = input("Introduce una palabra: ").upper()

# Recorrer cada letra de la palabra
for letra in palabra_usuario:
    # Saltar las vocales
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    
    # Mostrar solo consonantes
    print(letra)