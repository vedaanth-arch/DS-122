
#merge sort 
def MS(list): #this function  divides list
    if len(list)==1: 
        return list
    mid=len(list)//2
    left=MS(list[:mid])
    right=MS(list[mid:])
    return mergesort(left,right)


def mergesort(left,right):
    #this function sorts the list by merging the two halves
    i=j=0
    listy=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: #If left element is smaller, add to list
            listy.append(left[i]) #smaller element means appending to  listy
            i+=1
        else:
            listy.append(right[j])
            j+=1
#Here two more loops shuld be written bcz in above loop if any of one's 
# list is done ietrating then loop would come out and sorting would end 
    while i<len(left):
        listy.append(left[i])
        i+=1
    while j<len(right):
        listy.append(right[j])
        j+=1
    
    return listy

list= [10, 6, 9, 8, 2, 4, 7, 3, 5, 11]
print("Unsorted list:", list)
sorted_list = MS(list)  # Reassign the sorted array to a variable
print("Sorted list:", sorted_list)  # Print the sorted result




