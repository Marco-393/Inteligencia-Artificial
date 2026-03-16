hora = int(input("Introduce la hora inicial: "))
minutos = int(input("Introduce los minutos iniciales: "))
duracion = int(input("Duración del evento en minutos: "))

minutos = minutos + duracion
hora = hora + minutos // 60
minutos = minutos % 60
hora = hora % 24

print(f"{hora}:{minutos}")