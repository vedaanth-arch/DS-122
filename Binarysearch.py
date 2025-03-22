'''Binary search is a searching technique where the given data is found by dividing the list in two parts high and low 
and upon comparing when the values are not found the low and high counters are increased or decreased..'''
def binary_search(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif list[mid]>target: 
             high=mid-1 #searching the left half 
        elif list[mid]<target:
            low = mid + 1 #searching the right half
        return -1  #if the target is not found in the list for while loop
list=[23,4,54,32]   
a=binary_search(list,23)
print(a)  

print("BINARY SEARCH WHITH RECURSION")
def BS(l,key,lower=0,end=None):
    l.sort()
    end=len(l)-1
    mid = (lower+end)// 2
    if l[mid] == key:
        return mid
    elif l[mid]>key: 
        BS(l,key,lower,mid-1) #searching the left half 
    elif list[mid]<target:
        BS(l,key,mid+1,end) #searching the right half
    else:
        return -1  #if the target is not found in the list for while loop
l=[12,456,47468,768678,78960,89,9]
a=BS(l,456)
print(a)