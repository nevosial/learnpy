#Bubble Sort

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


#alist = [54,26,93,17,77,31,44,55,20]
alist = [0,13,5,923,67,81,39,63]
bubbleSort(alist)
print(alist)

#new list [0.34, 1.2, -1.2, 0, 4]
