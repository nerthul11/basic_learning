from random import *
from Funciones import holamundo

# 1. Imprimir "Hola mundo" por pantalla.
holamundo()

# 2. Crear dos variables numéricas, sumarlas y mostrar el resultado.
n1 = 5
n2 = 5
r = n1 + n2
print(r)

# 3. Mostrar el precio del IVA de un producto con el valor de 100 y su precio final.
IVA = 0.21
precio = 100
IVA *= precio
precio += IVA
print(f"El objeto vale {precio}, {IVA} son de IVA")

# 4. De dos números, saber cuál es el mayor.
n1 = int(input("Poné un número entero:"))
n2 = 19
if n1>n2:
    print(f"{n1} es mayor a {n2}.")
elif n1==n2:
    print(f"Son iguales.")
else:
    print(f"{n1} es menor a {n2}.")

# 5. Crea una variable numérica y si está entre 0 y 10, mostrar un mensaje indicándolo.
# 6. Añadir al anterior un mensaje para 11 a 20 y otro para 21 a 30.
if 0<=n1<=10:
    print("Está entre 0 y 10")
elif 11<=n1<=20:
    print("Está entre 11 y 20")
elif 21<=n1<=30:
    print("Está entre 21 y 30")

# 7. Mostrar con un while los números del 1 a n1
i = 0
while i!=n1:
    i+=1
    print(i)

# 8. Lo mismo que el 7 pero con for
for i in range(0,n1):
    i+=1
    print(i)
# 9. Mostrar los caracteres de la cadena "Hola mundo"
for i in "Hola mundo":
    print(i,end='')
print("\n")
# 10. Mostrar los números pares del 1 al 100
for i in range(2,101,2):
    print(i,end=' ')
print(".\n")
# 11. Generar un rango entre 0 y 10
rango = list(range(10))
print(rango)

# 12. Pop Quiiiiiz
n0 = randint(1,1000)
n1 = int(input("GUESS A NUMBER BETWEEN 1 AND 1000:"))
intentos = 5
while intentos>1:
    intentos -= 1
    if n0==n1:
        intentos=0
    elif n0>n1:
        print(f"BZZT!\nYOU HAVE {intentos} ATTEMPTS LEFT.")
        if n0-n1>=300:
            print(f"TIP: THE NUMBER IS WAAAAY HIGHER THAN {n1}")
        elif n0-n1>=100:
            print(f"TIP: THE NUMBER IS A LOT HIGHER THAN {n1}")
        elif n0-n1>=25:
            print(f"TIP: THE NUMBER IS SOMEWHAT HIGHER THAN {n1}")
        else:
            print(f"TIP: THE NUMBER IS JUST A BIT HIGHER THAN {n1}")
        n1 = int(input("INSERT A NUMBER BETWEEN 1 AND 1000:"))
    else:
        print(f"BZZT!\nYOU HAVE {intentos} ATTEMPTS LEFT.")
        if n1-n0>=300:
            print(f"TIP: THE NUMBER IS WAAAAY LOWER THAN {n1}")
        elif n1-n0>=100:
            print(f"TIP: THE NUMBER IS A LOT LOWER THAN {n1}")
        elif n1-n0>=25:
            print(f"TIP: THE NUMBER IS SOMEWHAT LOWER THAN {n1}")
        else:
            print(f"TIP: THE NUMBER IS JUST A BIT LOWER THAN {n1}")
        n1 = int(input("INSERT A NUMBER BETWEEN 1 AND 1000:"))


if n0==n1:
    print("YOU WIN!!")
else:
    print(f"LOSER! THE NUMBER WAS {n0}")