
from arbol import Arbol
from perro import Perro
from serpiente import Serpiente 
from raiz import SerVivo


perro_1 = Perro("Canis lupus familiaris",9,100,"bzbzbz","carnivoro","habitad","si","endoesqueleto oseo","cerdas","2 meses","doberman",100)
Serpiente_2 = Serpiente("Crotalus",13,120,"shshshsh","carnivoro","zonas aridas","si","endoesqueleto oseo","si","quilladas","2 metros","no")
arbol_3 = Arbol("solanum betaceum",7,100,"fiufiufiu","grandes perenmes","semi sombra","flores pequeñas","leñoso","ovoides","3 metros")

perro_1.ladrar()

Serpiente_2.atacar()

arbol_3.mudar_hojas()


perro_1.desplazarse()

print(f"la energia del perro es: {perro_1.energia}")

servivo_1 = SerVivo("Homo sapiens", 30, 100, "AGCTAGCTAGCTAGCT")


