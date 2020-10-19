'''
print("Hola, bienvenido a la calculadora Python. Aquí podrás realizar operaciones básicas.")

cuenta = input("Inserte la operación a realizar: +, -, *, /: ")
num1 = float(input("Inserte el primer número: "))
num2 = float(input("Inserte el segundo número: "))

if cuenta=="+":
    resultado=num1+num2
elif cuenta=="-":
    resultado=num1-num2
elif cuenta=="*":
    resultado=num1*num2
elif cuenta=="/":
    resultado=num1/num2
else:
    print("La operación insertada es incorrecta o no es trabajada por este programa.")

print(resultado)
'''

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [float(input(f'Ingresar valor {i+1} =')) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        s = a + b
        print(s)

    def resta(self):
        a,b =self.datos
        r = a - b
        print(r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print(math.sqrt(a))

num = raiz()
num.ingresardato()
print(num.cuadrada())