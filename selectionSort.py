//Selection Sort

def selectionSort(alist):
   for filler in range(len(alist)-1,0,-1):
       indexMax=0
       for location in range(1,filler+1):
           if alist[location]>alist[indexMax]:
               indexMax = location

       temp = alist[filler]
       alist[filler] = alist[indexMax]
       alist[indexMax] = temp

alist = [68,26,83,11,77,91,44,35,2]
selectionSort(alist)
print(alist)
