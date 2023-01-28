#pregunta9
class Vertice:
  def _init_(self, nombre):
    self.nombre = nombre
    self.planetas = {}
  
  def agregarPlaneta(self, planeta, distancia=0):
    self.vplanetas[planeta] = distancia
  
  def _str_(self):
    return f"{self.nombre}"

class Grafo:
  def _init_(self):
    self.vertices = {}
  
  def agregarVertice(self, vertice):
    self.vertices[vertice.nombre] = vertice
  
  def agregarArista(self, desde, hasta, distancia=0):
    if desde not in self.vertices:
      self.agregarVertice(Vertice(desde))
    if hasta not in self.vertices:
      self.agregarVertice(Vertice(hasta))
    self.vertices[desde].agregarVecino(self.vertices[hasta], distancia)
    self.vertices[hasta].agregarVecino(self.vertices[desde], distancia)
  
  def obtenerVertice(self, nombre):
    if nombre in self.vertices:
      return self.vertices[nombre]
    return None
  
  def arbolExpansionMinimaKruskal(self):
    arbol = Grafo()
    aristas = []
    for vertice in self.vertices.values():
      for planeta, distancia in vertice.planetas.items():
        aristas.append((distancia, vertice, planeta))
    aristas = sorted(aristas)
    conjuntos = {vertice: vertice.nombre for vertice in self.vertices.values()}
    for distancia, vertice, planeta in aristas:
      if conjuntos[vertice] != conjuntos[planeta]:
          arbol.agregarArista(vertice.nombre, planeta.nombre, distancia)
      for vertice in conjuntos:
        if conjuntos[vertice] == conjuntos[planeta]:
            conjuntos[vertice] = conjuntos[vertice]
        return arbol
  def _str_(self):
    s = ""
    for vertice in self.vertices.values():
        s += f"{vertice.nombre} -> {vertice.planetas.keys()} -> {vertice.planetas.values()}n"
    return s
  def generarGrafo(self, n, m):
    for i in range(n):
      self.agregarVertice(Vertice(i))