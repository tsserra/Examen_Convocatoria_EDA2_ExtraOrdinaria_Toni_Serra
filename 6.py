#ejercicio 6

def mochila_01(precio, pesos, pesomaximo):
    n = len(precio)
    tabla = [[0 for i in range(pesomaximo + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, pesomaximo + 1):
            if pesos[i-1] <= w:
                tabla[i][w] = max(precio[i-1] + tabla[i-1][w-pesos[i-1]], tabla[i-1][w])
            else:
                tabla[i][w] = tabla[i-1][w]
    return tabla[n][pesomaximo]