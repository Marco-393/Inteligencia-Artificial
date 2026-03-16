bloques = int(input("Introduce el número de bloques: "))
altura_piramide = 0
nivel = 1

while True:
    if bloques < nivel:
        break

    bloques = bloques - nivel
    altura_piramide = altura_piramide + 1
    nivel = nivel + 1

print("Altura total de la pirámide:", altura_piramide)