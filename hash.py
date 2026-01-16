'''
lista_contatos = dict()

for i in range(5):
    nome = input('Insira o nome do contato: ')
    telefone = input('Número do contato: ')
    print('-------------------------------')

    lista_contatos[nome] = telefone

print(lista_contatos.get(2))
'''

import requests

cache = {}

def pega_pagina(url):

    if cache.get(url):
        return cache[url]
    else:
        dados = requests.get(url)
        response = dados.text

        cache[url] = response
        return response

print(pega_pagina("https://instagram.com/"))