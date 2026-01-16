
def maisVendido(arr):
    mais_vendido = arr[0]['quantidade-vendida']
    indice_maior = 0

    for i in range(1, len(arr)):
        if(arr[i]['quantidade-vendida'] > mais_vendido):
            mais_vendido = arr[i]['quantidade-vendida']
            indice_maior = i
    return indice_maior

def ordenar(arr):
    novaLista = []

    for i in range(len(arr)):
        maior = maisVendido(arr)
        novaLista.append(arr.pop(maior))
    return novaLista


listaProdutos = []

for i in range(5):

    produto = input('Nome do produto: ')
    quantidade_vendida = int(input('Quantidade vendida do produto: '))
    print("------------------------------------------")

    dic = {
        'produto': produto,
        'quantidade-vendida':quantidade_vendida
        }
    
    listaProdutos.append(dic)

produosMaisVendidos = ordenar(listaProdutos)

print('Lista de produtos mais vendidos')
for p in produosMaisVendidos:
    print(p['produto'], '|', p['quantidade-vendida'], ' unidades')
    print('-------------------------------------')