from reptil import Reptil

class Serpiente(Reptil):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, venenoso, tipo_escamas, longitud_m, constructora):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, venenoso, tipo_escamas)
        self.longitud_m = longitud_m
        self.constructora = constructora

    def atacar (self):
        if self.venenoso == "si":
            print("da mordida venenosa")
        if self.constructora == "si":
            print("axficia a la presa")

    def desplazarse(self):
        print("desplazandose en sixseven")







