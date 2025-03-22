#26.Write a Python program to take a list of employee no. of working hours and 
#find number of employees who worked more than 6 hours using Linear search.

def emplyoement(hours_list):
    count = 0
    for hour in hours_list:
        if hour > 6:
            count += 1
    return count

# Main program
employee_hours = [5.5, 7.0, 6.5, 8.0, 4.0, 7.5]  # Example input
result = emplyoement(employee_hours)

print("Number of employees who worked more than 6 hours:", result)
