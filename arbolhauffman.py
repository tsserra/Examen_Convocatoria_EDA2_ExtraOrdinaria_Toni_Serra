#ejercicio 8
import heapq
mensajes = {"A":"0.2", "F":"0,17", "1":"0,13", "3":"0,21", "0":"0,05", "M":"0,09", "T":"015"}  
def construccion_arbol_hauffman(mensajes):
    lista_frecuencias = [(mensajes.count(char), char) for char in set(mensajes)]
    heapq.heapify(lista_frecuencias)
    while len(lista_frecuencias) > 1:
        nodo_izquierda = heapq.heappop(lista_frecuencias)
        nodo_derecha = heapq.heappop(lista_frecuencias)
        nodo = (nodo_izquierda[0] + nodo_derecha[0], nodo_izquierda, nodo_derecha)
        heapq.heappush(lista_frecuencias, nodo)
    return lista_frecuencias[0]