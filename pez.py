from vertebrado import Vertebrado

class Pez(Vertebrado):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_agua):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto)
        self.tipo_agua = tipo_agua

    def desplazarse (self):
        print|("Nada rapidamente")

    def respirar (self):
        print("filtrando agua por las branqueas")

