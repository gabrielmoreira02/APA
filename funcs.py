import numpy

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




