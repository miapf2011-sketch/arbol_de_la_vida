from mamifero import Mamifero

class Perro(Mamifero):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_pelaje, meses_gestacion, raza, nivel_lealtad):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, tipo_pelaje, meses_gestacion)
        self.raza = raza
        self.nivel_lealtad =nivel_lealtad

    def ladrar (self):
        print("defendiendo el territorio")




