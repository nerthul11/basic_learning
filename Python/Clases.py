class Pokemon:
    def __init__(self,name,species,type1,type2):
        self.name = name
        self.species = species
        self.type1 = type1
        self.type2 = type2

class Pikachu(Pokemon):
    def __init__(self):
        Pokemon.__init__(self,'Pikachu',25,'Electric',None)
        self.move1 = 'Thundershock'
        self.move2 = 'Swift'
        self.move3 = 'Rain Dance'
        self.move4 = 'Hurricane'

    def evolve(self):
        return Pokemon.__init__(self,'Raichu',26,'Electric',None)

    def __str__(self):
        return f'{self.name} ({self.species}) {self.move1}'


juanito = Pikachu() # Elegis bicho
setattr(juanito,'move1','Thunder') # Cambiás move 1
print(f'{juanito}')