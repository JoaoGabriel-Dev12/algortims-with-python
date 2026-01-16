

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = ["Alex", "Bianca", "Joao"]
result = pesquisa_binaria(minha_lista, "Bianca")

if result != None:
    print("Usuário", minha_lista[result], "encontrado")
else:
    print("usuario nao encontrado")