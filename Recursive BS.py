def binary_search(arr, low, high, x):
	# Check base case
	if high >= low:
		mid = (high + low) // 2
		# If element is present at the middle itself
		if arr[mid] == x:
			return mid
		# If element is smaller than mid, then it can only be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		# Element is not present in the array
		return None

# Test array
arr = [ 1,2,3,4,5,6,7,8,9,10]
x = int(input("Enter a number to find a number in a list of 1-10 numbes:"))

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result!= None:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")