'''Linear search is searching method where the whole list is searched by the key value'''
def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
            return ("Not in listt")
list=[12,456,47468,768678,78960,89,9]
b=linear_search(list,12)
print("Value found at index",b)

print("Linear search by recurssion")
def LSR(l,index,key):
    if index==-1:
        return -1
    elif l[index]==key:
        return index
    return LSR(l,index-1,key)
my_list = [3, 1, 4, 1, 5, 9, 2]
index = len(my_list) - 1
key = 5
result = LSR(my_list, index, key)
print(result)  # Output: 4
if result!=-1:
    print("Value found at index",result)
else:
    print("Value not found in list")