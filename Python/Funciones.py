# 1. Realiza una función que imprima 'Hola Mundo'
def holamundo():
    print('Hola Mundo!')
# 2. Realiza una función que sume dos números pasados por parámetros
def sumador(a,b):
    return a+b
# 3. Realiza una función que indique si un número pasado por parámetro es par o impar.
def espar(a):
    return (a%2 == 0)
# 4. Hacer una función que nos genere un número aleatorio entre dos parámetros pasados.
from random import * # Importa de una librería llamada random, ya existe
def azar(a,b):
    if a > b:
        c = a
        a = b
        b = c
    return randint(a,b) # randint es una función de la librería random
# 5. Crea una función que calcule el factorial de un número pasado por parámetro.
def factorial(a):
    resultado = a
    for i in range(a-1,1,-1):
        resultado = resultado * i
    return resultado
# 6. Crea una función que dados dos números mostrará todos los números que hay entre ellos.
def contador(a,b):
    for i in range(a+1,b):
        print(i)
        i+=1