import random
equipos = []

print("Este script te organiza un fixture, ponele.")
n = None
while not(n):
    try:
        n = int(input("Empecemos por definir la cantidad de equipos: "))
    except ValueError:
        print("Que sea un número.")
        continue
    if n<=3:
        print("Debería ser un número mayor o igual a 4")
        n = None
        continue
    if (n%2 == 1):
        print("Debería ser un número par.")
        n = None
        continue
    if n>32:
        choice = int(input("Esos son bastantes equipos, estás seguro que querés ese número? Sí = 0, No = 1:"))
        if choice != 0:
            n = None

for i in range(n):
    e = input(f"Nombre del equipo {i + 1}:")
    while e in equipos:
        print("Ese nombre ya está utilizado, probá otro.")
        e = input(f"Nombre del equipo {i + 1}:")
    while not(e):
        e = input(f"Nombre del equipo {i + 1}:")
    equipos.insert(i,e)

random.shuffle(equipos)
print("Los enfrentamientos son los siguientes:")

i=0
vs=1
while i<n:
    print(f"{vs}- {equipos[i]} vs {equipos[i+1]}")
    i+=2
    vs+=1