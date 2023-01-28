#pregunta 2 y 3
class armadura():
    def _init_(self,nombre,rango):
        self.nombre = nombre
        self.rango = rango
    def constructor(self):
        self.armadura=print(self.nombre, " ha creado una armadura de rango ", self.rango)    
    def __str__(self):
        return f"{self.nombre} {self.rango}"
class Codigolegion(armadura):
    def _init_(self, nombre, rango, codigolegion:str) -> None:
        super()._init_(nombre, rango,codigolegion)
        self.codigolegion=codigolegion
class Identificador_coherente(armadura):
    def _init_(self,nombre,rango,identificadorcoherente:int) -> None:
        super()._init_(nombre,rango,identificadorcoherente)
        self.identificadorcoherente=identificadorcoherente
class Identificador_siglo(armadura):
    def _init_(self, nombre, rango,identificadorsiglo):
        super()._init_(nombre,rango,identificadorsiglo)
        self.identificadorsiglo=identificadorsiglo
class Identificador_escuadra(armadura):
    def _init_(self, nombre, rango,identificadorescuadra):
        super()._init_(nombre,rango,identificadorescuadra)
        self.identificadorescuadra=identificadorescuadra
class Identificador_armadura(armadura):
    def _init_(self, nombre, rango,identificadorarmadura):
        super()._init_(nombre,rango,identificadorarmadura)
        self.identificadorarmadura=identificadorarmadura


 
miArmadura = armadura("Toni", "100")
tuArmadura = armadura("Ruben", "-1")
lista = list(miArmadura.__str__, tuArmadura.__str__)
print(lista)