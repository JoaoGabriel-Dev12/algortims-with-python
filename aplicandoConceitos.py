


'''
def busca_em_largura(inicio):
    fila = deque()
    fila += grafo[inicio]
    verificadas = set()

    while fila:
        pessoa = fila.popleft()
        if not pessoa in verificadas:
            if(pessoa == "ana"):
                return True
            else:
                fila += grafo[pessoa]
                verificadas.add(pessoa)
    return False


grafo = {
    "voce": ["joao", "maria", "pedro"],
    "joao": ["carlos", "ana"],
    "maria": ["paula"],
    "pedro": [],
    "carlos": [],
    "ana": [],
    "paula": []
}

print(busca_em_largura("voce"))
'''

from collections import deque

def menor_caminho(inicio, destino):
    salas = deque()
    salas.append((inicio, 0))
    salas_verificadas = set()

    while salas:
        sala, passos = salas.popleft()
        if not sala in salas_verificadas:
            if sala == destino:
                return passos
            else:
                salas_verificadas.add(sala)
                for vizinho in grafo[sala]:
                    salas.append((vizinho, passos + 1))
    return -1


grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(menor_caminho("A", "F"))
