#35.Write a Python program to analyse the frequency distribution in sorted list
def afd(sorted_list):
    frequency_distribution = {}

    for element in sorted_list:
        if element in frequency_distribution:
            frequency_distribution[element] += 1
        else:
            frequency_distribution[element] = 1

    return frequency_distribution

# Example usage
sorted_list = [1, 1, 2, 2, 2, 3, 4, 4, 5]
frequency_distribution = afd(sorted_list)

print("Frequency Distribution:")
for element, frequency in frequency_distribution.items():
    print(f"Element: {element}, Frequency: {frequency}")
