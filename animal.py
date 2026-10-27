from raiz import SerVivo

class Animal(SerVivo):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.tipo_dieta =tipo_dieta
        self.habitat = habitat

    def desplazarse(self):
        self.energia = -5
        print("el animal se mueve -5 de energia")

    def alimentarse(self):
        if self.tipo_dieta == "carnivoro":
            self.energia = +20
            print("cazando presa")
        else:
            self.energia = +20
            print("comiendo plantas")




    