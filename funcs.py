
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



def quickSort(alist):

  quickSortHelper(alist,0,len(alist)-1)
  return alist

def quickSortHelper(alist,first,last):

  if first<last:
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark