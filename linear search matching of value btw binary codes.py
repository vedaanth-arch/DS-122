'''25.	Write a Python program to take 2 binary strings of length ‘n’ as input and find no of values matched using Linear search.
Eg: a=1010
       B=0100
o/p=1
'''
def LSS(a,b):
    n=len(a)
    m=len(b)
    a1=list(a)
    b1=list(b)
    print("the first given list:",a1)
    print("the second given list:",b1)
    count=0
    for i in (a1):
       for j in (b1):
           if i==j:
            count+=1
            print("Matching element:", i)
            return 
    if count:  # Check if count has any matches
        print("Matching elements:", count)
    else:
        print("No elements matching")
a="1010"
b="0100"
LSS(a,b)        
        