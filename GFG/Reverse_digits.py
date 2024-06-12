class Solution:
    def reverse_digit(self, N):
        # Step 1: Convert the number to a string
        str_N = str(N)
    
        # Step 2: Reverse the string
        reversed_str_N = str_N[::-1]
    
        # Step 3: Convert the reversed string to an integer to remove leading zeroes
        reversed_N = int(reversed_str_N)
    
        # Step 4: Return the integer
        return reversed_N

N1 = 200
N2 = 122
N3 = 12345000

# Example usage
obj = Solution()
print(obj.reverse_digit(N1))  # Output: 2
print(obj.reverse_digit(N2))  # Output: 221
print(obj.reverse_digit(N3))  # Output: 54321
