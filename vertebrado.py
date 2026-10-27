from animal import Animal

class Vertebrado(Animal):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat)
        self.tiene_columna = tiene_columna
        self.tipo_esqueleto = tipo_esqueleto




