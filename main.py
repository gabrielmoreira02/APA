import time
from funcs import *


def marcadordetempo(function):
    start = time.time()
    print(function(numeros))
    end = time.time()
    timespent = end - start
    print("o tempo gasto pela funcao foi:", timespent)
    return

while True:
    tipo = int(input("Qual funcao voce deseja testar? (1 para selectionSort, 2 para insertionSort, 3 para mergeSort, 4 para quickSort,"
                     "5 para countingSort, 6 para radix e 7 para heap):     "))
    qtd = int(input("Com quantos elementos voce deseja testar?(100, 1000, 10000 ou 100000):            "))

    if qtd == 100:
        filename = "couting.txt"
    elif qtd == 1000:
        filename = "num.1000.1.in"
    elif qtd == 10000:
        filename = "num.10000.1.in"
    elif qtd == 100000:
        filename = "num.100000.1.in"
    else:
        print("Valor errado")
        continue


    file = open(filename, "r")
    numeros = []
    for line in file:
        numeros.append(int(line))
    numeros = numeros[1:]


    if tipo == 1:
        print(len(numeros))
        marcadordetempo(selectionSort)
    elif tipo == 2:
        marcadordetempo(insertionSort)
    elif tipo == 3:
        marcadordetempo(mergeSort)
    elif tipo == 4:
        marcadordetempo(quickSort)
    elif tipo == 5:
        marcadordetempo(countingSort)
    elif tipo == 6:
        marcadordetempo(radix_sort)
    elif tipo == 7:
        marcadordetempo(heapSort)
    else:
        print("opcao invalida")
        continue








