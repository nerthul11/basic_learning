class Animal:
    def __init__(self,especie):
        self.especie = especie

    def getEspecie(self):
        return f'La especie de este animal es: {self.especie}'

    def setEspecie(self):
        self.especie = input('¿Qué especie es? ')

    def printMensaje(self):
            return f'Este es un animal no clasificado.'

class Perro(Animal):
    def __init__(self,raza):
        Animal.__init__(self,'Perro')
        self.raza = raza

    def getRaza(self):
        return f'La raza de este perro es {self.raza}'

    def setRaza(self):
        self.raza = input('¿Qué raza es? ')

    def printMensaje(self):
        return f'Este es un perro y su raza es {self.raza}'

class Pez(Animal):
    def __init__(self,alimentacion):
        Animal.__init__(self,'Pez')
        self.alimentacion = alimentacion

    def getAlimentacion(self):
        return f'Este pez come {self.alimentacion}'

    def setAlimentacion(self):
        self.alimentacion = input('¿Qué come? ')

    def printMensaje(self):
        return f'Este es un pez que come {self.alimentacion}'

class Serpiente(Animal):
    def __init__(self,venenosa):
        Animal.__init__(self,'Serpiente')
        self.venenosa = venenosa

    def isVenenosa(self):
        if self.venenosa:
            return True
        else:
            return False

    def setVenenosa(self):
        self.venenosa = True

    def printMensaje(self):
        if self.venenosa:
            return 'Esta es una serpiente venenosa.'
        else:
            return 'Esta es una serpiente, pero no es venenosa.'