from vertebrado import Vertebrado

class Ave(Vertebrado):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto, verga_dura_alas, volar):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_columna, tipo_esqueleto)
        self.verga_dura_alas = verga_dura_alas
        self.volar = volar

    def desplazarse(self):
        if self.volar == "si":
            print("volando")
            self.energia = -15
        else:
            print("caminando rapido")
            self.energia = -15




