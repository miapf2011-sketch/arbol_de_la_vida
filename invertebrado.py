from animal import Animal

class Invertebrado(Animal):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_exoesqueleto, numero_patas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat)
        self.tiene_exoesqueleto =tiene_exoesqueleto
        self.numero_patas = numero_patas


