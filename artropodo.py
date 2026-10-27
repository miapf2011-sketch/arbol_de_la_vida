from invertebrado import Invertebrado

class Artropodo(Invertebrado):
    def __init__(self, nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_exoesqueleto, numero_patas, alas, numero_antenas):
        super().__init__(nombre_cientifico, edad, energia, adn, tipo_dieta, habitat, tiene_exoesqueleto, numero_patas)
        self.alas = alas
        self.numero_antenas =numero_antenas

    def mudar_exoesqueleto (self):
        print("desecha la coraza vieja para crecer")
        self.energia = -20





