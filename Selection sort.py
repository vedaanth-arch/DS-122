# Define a function called selectionSort that takes an array and its size as parameters
# This function will sort the array in ascending order using the selection sort algorithm
def selectionSort(array, size):
    # Iterate over the array from the first element to the second last element
    # This is because the last element will be in its correct position after the second last iteration
    for ind in range(size):
        # Initialize the minimum index to the current index
        # We assume the current element is the smallest, and then compare it with the rest of the elements
        min_index = ind
        # Iterate over the unsorted part of the array (from the current index + 1 to the end)
        # We only need to consider the unsorted part because the sorted part is already in order
        for j in range(ind + 1, size):
            # If the current element is smaller than the element at the minimum index, update the minimum index
            # We update the minimum index to keep track of the smallest element in the unsorted part
            if array[j] < array[min_index]:
                min_index = j
        # Swap the element at the current index with the element at the minimum index
        # This is the key step in selection sort, where we move the smallest element to its correct position
        array[ind], array[min_index] = (array[min_index], array[ind])

# Create an array of integers
arr = [2, 45, 0, 11, 9, 88, 97, 202, 747]
# Get the size of the array
# We need the size to pass it to the selectionSort function
size = len(arr)

# Call the selectionSort function to sort the array
selectionSort(arr, size)

# Print the sorted array
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)