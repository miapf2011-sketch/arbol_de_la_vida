from planta import Planta

class PlantaVascular(Planta):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, flor, tipo_tallo):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra)
        self.flor =flor
        self.tipo_tallo =tipo_tallo

    def transportar_savia (self):
        print("transporta nutrientes")
        self.energia = +5



