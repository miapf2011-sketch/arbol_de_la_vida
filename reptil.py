from vertebrado import Vertebrado

class Reptil(Vertebrado):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, venenoso, tipo_escamas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto)
        self.venenoso = venenoso
        self.tipo_escamas = tipo_escamas

    def desplazarse(self):
        print("reptando o arrastrandose")


