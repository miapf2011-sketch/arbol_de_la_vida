from raiz import SerVivo

class Hongo(SerVivo):
    def __init__(self, nombre_cientifico, edad, energia, adn, venenoso):
        super().__init__(nombre_cientifico, edad, energia, adn)
        self.venenoso = venenoso

    def alimentarse(self):
        print("esta descomponiendo")




    