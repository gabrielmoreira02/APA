import time


def selectionSort(lista):
    for i in range(len(lista)):
        minPosition = i

        for j in range(i + 1, len(lista)):
            if lista[minPosition] > lista[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        temp = lista[i]
        lista[i] = lista[minPosition]
        lista[minPosition] = temp
    return lista

def insertionSort(lista):
    for index in range(1,len(lista)):

        currentvalue = lista[index]
        position = index

        while position>0 and lista[position-1]>currentvalue:
             lista[position]=lista[position-1]
             position = position-1

        lista[position]=currentvalue
    return lista