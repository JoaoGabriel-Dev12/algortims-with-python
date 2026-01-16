'''
def fat(i):
    if(i <= 1):
        return 1# Caso-base
    else:
        return i * fat(i-1) # Caso-recursivo
x = fat(5)
print(x)


def saudacao(nome):
    print("Ola " +nome)
    saudacao2(nome)
    print("Preparando despedida...")
    despedida()

def saudacao2(nome):
    print("Prazer em te conhecer, " +nome)

def despedida():
    print("Até mais, bye bye!")

saudacao("João Gabriel")
'''

def fibonnaci(num):
    if num <= 1:
        return num
    else:
        return fibonnaci(num-2) + fibonnaci(num -1)

print(fibonnaci(1))