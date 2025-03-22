def sort_digits(numbers):
    result = []
    for num in numbers:
        # The number num is converted to a string,and each character(digit)is
        #converted back to an integer and stored in the list digits.
        #This line essentially creates a list of the individual digits of the number.
        digits = [int(d) for d in str(num)]
        # Initialize count array
        count = [0] * 3
        # Count occurrences of each digit
        for digit in digits:
            count[digit] += 1
        # Build the sorted number
        sorted_num = '' #An empty string 
        for i in range(3):
            sorted_num += str(i) * count[i]
            # For each index i,it adds the digit i to sorted_num a number of times equal to count[i].
            #This effectively builds a string that represents the digits in sorted order.
        # Convert back to integer and append to the result list
        result.append(int(sorted_num))
        #The sorted_num string is converted back to an integer and appended to the result list.
    return result

# Input array
input_array = [102, 201, 210, 121]

# Call the function and print the result
output_array = sort_digits(input_array)
print("Input:", input_array)
