matriz = [
    [30, 5, 80],
    [120, 9, 70],
    [100, 35, 44]
]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def ordenar_fila_con_quicksort(matriz, fila):
    matriz[fila] = quicksort(matriz[fila])


fila_a_ordenar = 1
ordenar_fila_con_quicksort(matriz, fila_a_ordenar)
for fila in matriz:
    print(fila)