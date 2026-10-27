from planta import Planta

class PlantaNoVascular(Planta):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra, crece_roca):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_hoja, necesita_sombra)
        self.crece_roca =crece_roca

    def alimentarse(self):
        print("absorviendo humedad")




        
