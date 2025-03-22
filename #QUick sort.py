#QUick sort
def QS(list,low,high):
    if low<high:
        p=quicksort(list,low,high)
         # Separately sort elements before 
        # partition and after partition 
        quicksort(list, low, p-1) 
        quicksort(list, p+1, high) 
    
def quicksort(list,low,high):
    n=len(list)
    pivot=list[high]
    i=(low-1) ## index of smaller element
    for j in range(low,high):
        #If current element is smaller than or equal to pivot 
        if list[j]<=pivot:
            #increment index of smaller element 
            i+=1
            #Swap current element with greater element, i.e., element at index
            list[i],list[j] =list[j],list[i] #ensuring that elements smaller than or equal to the pivot are on the left side of the array
    
    # Place the pivot in the correct position
    if i + 1 < len(list):  # Ensure i + 1 is within bounds
        list[i + 1], list[high] = list[high], list[i + 1]  # Swap pivot to correct position

     #the pivot element is placed in the correct position: 
    #everything on its left is smaller, and everything on its right is larger.
    #i+1 represents the first position where an element greater than the pivot has been found
    return ( i+1 ) 

#Test the code
list = [64,34,25,12,22,11,90]
QS(list,0,len(list)-1)
for i in range(len(list)): 
    print("%d" % list[i])
