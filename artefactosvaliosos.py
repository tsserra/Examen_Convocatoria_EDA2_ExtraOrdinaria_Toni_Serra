#ejercicio4
class artefactosvaliosos():
    def __init__(self, peso, nombre, precio, fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
    def constructor(self):
        self.conserva = print("Se ha creado la conserva ", self.nombre, " de ", self.peso, "que caduca: ", self.fecha, " y cuesta:", self.precio)
    def _str_(self):
        return f"{self.nombre} {self.peso} {self.precio} {self.fecha}"      

ConservaAtun = artefactosvaliosos("50g", "Atún", "30€", "10-12-23")
ConservaJudias = artefactosvaliosos("100g", "Judias", "20€", "22-02-23" )
Consulta = ConservaJudias.__str__(), ConservaAtun.__str__()
ConservaJudias.constructor()
ConservaAtun.constructor()
print(Consulta)