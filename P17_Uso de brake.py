# Palabra secreta
clave = "chupacabra"

# Bucle que pide palabras hasta acertar
while True:
    entrada = input("Introduce una palabra: ")

    if entrada == clave:
        print("Saliste del bucle correctamente.")
        break