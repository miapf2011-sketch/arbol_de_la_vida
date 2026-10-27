from planta_vascular import PlantaVascular

class Arbol(PlantaVascular):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, flor, tipo_tallo, da_frutos, altura_m):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, flor, tipo_tallo)
        self.da_frutos = da_frutos
        self.altura_m = altura_m

    def mudar_hojas (self):
        if self.tipo_hoja == "caduca":
            print("dejar caer  hojas")
        else:
            print("mantenerlas")



