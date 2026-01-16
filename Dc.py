
def soma(arr):

    if len(arr) == 0:
        return 0
    else:
        return arr[0] + soma(arr[1:])
    

def  contador(arr):

    if len(arr) == 0:
        return 0
    else:
        return 1 + contador(arr[1:])
    
print(soma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(contador([1, 2, 3, 4]))


def valor_mais_alto(arr):
    if(len(arr) == 2):
        return arr[0] if arr[0] > arr[1] else arr[1]
    maximo = valor_mais_alto(arr[1:])
    return arr[0] if arr[0] > maximo else maximo

print(valor_mais_alto([2, 6, 3, 10, 7]))