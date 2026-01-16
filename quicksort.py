
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(maiores) + [pivo] + quicksort(menores)

print(quicksort([2, 3, 1, 5, 4, 6, 9, 8, 7]))