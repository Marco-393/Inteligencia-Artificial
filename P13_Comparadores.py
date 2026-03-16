# Pedir el nombre de una planta
flor = input("Escribe el nombre de una planta: ")
nombre = flor

# Evaluar la respuesta
if nombre == "ESPATIFILO":
    print("Sí, ¡ESPATIFILO es la mejor planta que existe!")
elif nombre == "espatifilo":
    print("No, ¡quiero un Espatifilo con mayúsculas!")
else:
    print("¡Espatifilo!, ¡No", nombre + "!")