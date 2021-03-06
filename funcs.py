import numpy


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # BUILDMAXHEAP
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    #Ordenacao
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr







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
    for i in range(1,len(lista)):

        currentvalue = lista[i]
        position = i

        while position>0 and lista[position-1]>currentvalue:
             lista[position]=lista[position-1]
             position = position-1

        lista[position]=currentvalue
    return lista

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergeSort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a,b)



def quickSort(lista):

  quickSortHelper(lista,0,len(lista)-1)
  return lista

def quickSortHelper(lista, first, last):

  if first<last:
      splitpoint = partition(lista,first,last)
      quickSortHelper(lista,first,splitpoint-1)
      quickSortHelper(lista,splitpoint+1,last)

def partition(lista,first,last):

  pivotvalue = lista[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = lista[leftmark]
          lista[leftmark] = lista[rightmark]
          lista[rightmark] = temp

  temp = lista[first]
  lista[first] = lista[rightmark]
  lista[rightmark] = temp

  return rightmark



def countingSort(lista):

    c=[]
    b=[0]*len(lista)
    menor = min(lista)

    if(menor<= 0):
        for i in range(0, len(lista)):
            lista[i] = lista[i] - menor


    for j in range(0, max(lista)+1):
        c.append(0)

    for i in range(0, len(lista)):
        c[lista[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in reversed(range(0, len(lista))):
        b[c[lista[i]]-1] = lista[i]
        c[lista[i]] -= 1

    if(menor<= 0):
        for i in range(0, len(b)):
            b[i] = b[i] + menor

    print(len(b))
    return b


def counting_sort(arr, max_value, get_index):
    counts = [0] * max_value

    # Counting - O(n)
    for a in arr:
        counts[get_index(a)] += 1


    # Accumulating - O(k)
    for i, c in enumerate(counts):
        if i == 0:
            continue
        else:
            counts[i] += counts[i - 1]

    # Calculating start index - O(k)
    for i, c in enumerate(counts[:-1]):
        if i == 0:
            counts[i] = 0
        counts[i + 1] = c

    ret = [None] * len(arr)
    # Sorting - O(n)
    for a in arr:
        index = counts[get_index(a)]
        ret[index] = a
        counts[get_index(a)] += 1

    return ret


def get_digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10

def get_num_difit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(lista):
    menor = min(lista)
    if(menor<= 0):
        for i in range(0, len(lista)):
            lista[i] = lista[i] - menor

    max_value = max(lista)
    num_digits = get_num_difit(max_value)

    for d in range(num_digits):
        lista = counting_sort(lista, max_value, lambda a: get_digit(a, d+1))

    if(menor<= 0):
        for i in range(0, len(lista)):
            lista[i] = lista[i] + menor

    return lista

