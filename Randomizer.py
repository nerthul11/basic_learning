import random

chance = 1000000
exito = random.randint(1,chance)
probabilidad_exito = 1
intento = 1
if probabilidad_exito>0:
    while exito>probabilidad_exito:
        print(f"Intento número {intento} (Número obtenido: {exito})")
        intento += 1
        exito = random.randint(1,chance)
    print(f"Intento número {intento} (Número obtenido: {exito})")
    print(f"Éxito al intento número {intento}")
else:
    print("Nunca va a funcionar")