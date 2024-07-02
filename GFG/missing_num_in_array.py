def find_missing_number(n, arr):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example 1
n = 5
arr = [1, 2, 3, 5]
print(find_missing_number(n, arr))  # Output: 4

# Example 2
n = 2
arr = [1]
print(find_missing_number(n, arr))  # Output: 2
