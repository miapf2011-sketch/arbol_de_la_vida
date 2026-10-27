class SerVivo:
    def __init__(self,nombre_cientifico,edad,energia,adn):
        self.nombre_Cientifico = nombre_cientifico
        self.edad = edad
        self.energia = energia
        self.adn = adn
    def getter_ADN(self):
        print(self.adn)
    def nacer(self):
        print("nacer")
        self.energia = 100
    def morir(self):
        self.energia = 0
        print("fallecio")
    def alimentarse(self):
        pass


