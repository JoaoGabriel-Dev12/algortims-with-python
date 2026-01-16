
def buscaMaior(arr):
    maior = arr[0]
    indice_maior = 0

    for i in range(1, len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            indice_maior = i

    return indice_maior

def ordenacao(arr):
    novoArr = []

    for i in range(len(arr)):
        maior = buscaMaior(arr)
        novoArr.append(arr.pop(maior))
    return novoArr

lista = [2, 9, 8, 10, 3, 5]
print(ordenacao(lista))