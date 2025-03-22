def BS(list,ele):
    low=0
    high=len(list)
    while low<high:
        mid=(low+high)//2
        if list[mid]<ele:
            low=mid+1
        else:
            high=mid
    return low
def isl(list,ele):
    pos=BS(list,ele)
    list.insert(pos,ele)
    return list

list=[1,2,4,7,9]
ele=5
NL=isl(list,ele)
print("Array after insertion:",NL)