from abc import ABC, abstractmethod
class SerVivo(ABC):
    def __init__(self,nombre_cientifico,edad,energia,adn):
        self.nombre_Cientifico = nombre_cientifico
        self.edad = edad
        self.adn = adn
        self._energia = max(0, min(energia, 100))
    def getter_ADN(self):
        print(self.adn)

    def setter_energia(self, energia):
        self.energia = energia

    def nacer(self):
        print("nacer")
        self._energia = 100
    def morir(self):
        self._energia = 0
        print("fallecio")
    @abstractmethod
    def alimentarse(self):
        pass
    @property
    def energia(self):
        return self._energia
    def estar_vivo(self):
        if self.energia > 0:
            return True
        else:
            return False
        
