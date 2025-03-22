#Counting sort
def CS(list):
    #taking max element
    maxele=max(list)
    place=1
    while (maxele//place)>0: #traversing till by floor division the value received is greater than zer0
        countingsort(list,place)
        place*=10 # as to increase the loop  by 10 times as we are dealing with decimal places
        return list

def countingsort(list,place):
    n=len(list)

    #building up count array
    count=[0]*10 #here 10 bcz only taken till 10(0-9)
    output=[0]*n

    #loop for step(1),count array 
    for i in range(n):
        index=(list[i]//place)%10 # to separate numbers
        count[index]+=1  #counting the numbers,incrementing
    
    #loop for cummulative array,step(2)
    for i in range(1,10):
        count[i]+=count[i-1] 
        # For each element count[i], 
        # it adds the value of the previous element count[i-1] to it.

    #Loop for output array,step(3)
    for i in range(n-1,-1,-1):
        index=(list[i]//place)%10 
        output[count[index]-1]=list[i]
        #places each element in it's sorted postion in output array
        #based upon the cummulative aray
        count[index]-=1
        #The line count[index]-=1 is decrementing the count array. Specifically, 
        # it's decrementing the value at the index position in the count array.

    for i in range(n):
        output[i]=list[i]
        #simply assigns each value from output to list 
    print(list)
list=[7, 10, 4, 3, 20, 15]
CS(list)




