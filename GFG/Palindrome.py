class Solution:
    def is_palindrome(self, n):
        x = str(n)
        if x == x[::-1]:
            return "Yes"
        return "No"
        
n = 123
# n = 555
obj = Solution()
print(obj.is_palindrome(n))