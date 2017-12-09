#Binary Search

def bSearch(alist, target):
    start = 0
    end = len(alist) - 1
    found = False
    
    while(start <= end) and not found:
        mid = (start+end)//2
        if alist[mid] == target:
            found = True
                    
        else:
            if target > alist[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
    return found


lists = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(bSearch(lists, 11))
print(bSearch(lists, 21))
