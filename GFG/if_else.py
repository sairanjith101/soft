n = 4
m = 8

class Solution:
    def compareNM(self, n : int, m : int):
        if n < m:
            return "lesser"
        elif n == m:
            return "equal"
        elif n > m:
            return "greater"
        
obj = Solution()
print(obj.compareNM(n,m))
