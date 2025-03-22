def MS(list):
    if len(list)<=1:
        return list
    mid=len(list)//2
    left=MS(list[:mid])
    right=MS(list[mid:])
    return mergesort(left,right)

def mergesort(left,right):
    i=j=0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    
    while i<len(left):
        res.append(left[i])
        i+=1

    while j<len(right):
        res.append(right[j])
        j+=1
    return res
 
left=[4,6,7,9]
right=[1,2,3,5]
merger=left+right
print(merger)
a=MS(merger)
print("the sorted array is:",a)

