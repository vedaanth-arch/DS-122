#Write a Python program to find the nth smallest element in the array [7, 10, 4, 3, 20, 15]
#here the nth smallest means after sorting the nth element will be the smallest and n pointer will
# be the  position of the nth smallest element in the array.

def MS(arr):
    if len(arr)<=1:
        return arr 

    mid = len(arr) // 2
    left = MS(arr[:mid])  # Recursively sort the left half
    right = MS(arr[mid:])  # Recursively sort the right half
    return mergesort(left, right)  # Merge the sorted halves

def mergesort(left, right):
    lenty = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lenty.append(left[i])
            i += 1
        else:
            lenty.append(right[j])
            j += 1

    # Append remaining elements from left
    while i < len(left):
        lenty.append(left[i])
        i += 1

    # Append remaining elements from right
    while j < len(right):
        lenty.append(right[j])
        j += 1

    return lenty

# Given array
arr = [7, 10, 4, 3, 20, 15]
sorted_array = MS(arr)
print("Sorted array:", sorted_array)

# Get the nth value from the user
n = int(input("Enter the nth value: "))
if 1 <= n <= len(sorted_array):
    print("The nth smallest element is:", sorted_array[n - 1])  # Access nth element
else:
    print("Invalid value for n, please enter a value between 1 and", len(sorted_array))





