from vertebrado import Vertebrado

class Mamifero(Vertebrado):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_pelaje, meses_gestacion):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto)
        self.tipo_pelaje = tipo_pelaje
        self.meses_gestacion = meses_gestacion

    def amamantar(self):
        print("aumenta la energia (jajajja nada)")

    def desplazarse(self):
        print("corriendo en cuatro patas")
        self.energia = -10




        