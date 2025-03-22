def RS(list):
    # Helper function for radix sort on non-negative numbers
    def radix_sort_positive(nums):
        maxele = max(nums)
        place = 1
        while maxele // place > 0:
            buckets = [[] for _ in range(10)]
            for num in nums:
                index = (num // place) % 10
                buckets[index].append(num)
            nums.clear()  # clear the list
            for bucket in buckets:
                nums.extend(bucket)
            place *= 10
        return nums

    # Separate positive and negative numbers
    positives = [num for num in list if num >= 0]
    negatives = [-num for num in list if num < 0]  # Convert to positive for sorting

    # Sort positive and negative numbers
    sorted_positives = radix_sort_positive(positives)
    sorted_negatives = radix_sort_positive(negatives)
    
    # After sorting negatives (in positive form), revert back to negative and reverse the list
    sorted_negatives = [-num for num in sorted_negatives][::-1]

    # Combine sorted negatives and positives
    return sorted_negatives + sorted_positives

# Test case with negative and positive numbers
list = [-170, 45, -75, 90, 802, -24, 2, -66]
res = RS(list)
print(res)
