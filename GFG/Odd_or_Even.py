class Solution:
    def oddEven (ob,N):
        if N % 2 == 0:
            return "even"
        else:
            return "odd"

N = int(input("Enter a  value: "))

obj = Solution()
print(obj.oddEven(N))