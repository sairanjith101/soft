def isBinary(s):
    for char in s:
        if char != '0' and char != '1':
            return 0
    return 1

# Example usage:
print(isBinary("101"))  # Output: 1
print(isBinary("75"))   # Output: 0
print(isBinary("171"))  # Output: 0

    