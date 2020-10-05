'''
Comillas largas para comments largos
'''

'''
integer = 10
float = 1.234
string = 'Str es un tipo de dato y una funcion'
booliano = True
buliano = False
print(integer, float, string, booliano, buliano)

'''
#Potencia es **, division redondeada // y resto %
'''
print("WELCOME TO THE SYSTEM")

nombre = input("PLEASE INSERT YOUR NAME:")
edad = int(input(f"I SEE, THANK YOU {nombre}, PLEASE INSERT YOUR AGE:"))

if 0<edad<120:
    if edad>=18:
        print(f"SO,{nombre}, YOU WILL BE {edad+10} YEARS OLD IN 10 YEARS")
    else:
        print(f"COME BACK IN {18-edad} YEARS")
else:
    print("STOP BULLSHITTING ME")
'''
'''
#WHILE
import math

numero = int(input("Quiero saber la raíz cuadrada de: "))

while numero<0:
    print("La raíz cuadrada de los negativos es un invento del capitalismo.")
    numero = int(input("Vamos de nuevo pero con un número en serio: "))

print(f"La raíz cuadrada de {numero} es {(math.sqrt(numero)):.2f}") # El 2f indica cuántos decimales
'''
#FOR
qwerty = {"Key":666,"Kaddan":1919,"WTF":0}

for a,b in qwerty.items(): # a y b son variables que se inventan y buscan en diccionario
    print(f"{a}: {b}")
