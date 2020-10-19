class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años.'

class Empleado(Persona):
    def __init__(self,sueldo):
        Persona.__init__(self,input('Nombre Empleado: '),input('Edad Empleado: '))
        self.sueldo = sueldo

    def impuesto(self):
        if self.sueldo >= 3000:
            return 'sí'
        else:
            return 'no'

    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años y cobra ${self.sueldo}, por lo tanto {self.impuesto()} le corresponde pagar impuestos.'

pers = Persona(input('Nombre Persona: '),int(input('Edad Persona: ')))
empl = Empleado(0)
setattr(empl,'sueldo',int(input('Sueldo Empleado: ')))
print(f'\n{pers}\n{empl}')