def findIndex(arr, n, key):
    # Initialize the start and end indices to -1
    start_index = -1
    end_index = -1
    
    # Traverse the array to find the first and last occurrence of the key
    for i in range(n):
        if arr[i] == key:
            if start_index == -1:
                start_index = i  # Set start index on first occurrence
            end_index = i  # Update end index on every occurrence
    
    # Return the start and end indices
    return [start_index, end_index]

# Example usage
n1 = 6
arr1 = [1, 2, 3, 4, 5, 5]
key1 = 5
print(findIndex(arr1, n1, key1))  # Output: [4, 5]

n2 = 6
arr2 = [6, 5, 4, 3, 1, 2]
key2 = 4
print(findIndex(arr2, n2, key2))  # Output: [2, 2]
