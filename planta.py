from raiz import SerVivo

class Planta(SerVivo):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.tipo_hoja = tipo_hoja
        self.necesita_sombra = necesita_sombra
    def alimentarse(self):
        self._energia += 10
        print ("esta haciendo fotosintesis")



