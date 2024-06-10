# Option 1

# def findsumofseries(n):

#     output = 0

#     for i in range(n+1):
#         output += i

#     return output

# n = int(input("Enter a value: "))

# print(findsumofseries(n))

class Solution:
    def findsumofseries(self, n):

        sumofseries = (n*(n+1))//2

        return sumofseries

n = int(input("Enter a value: "))

obj = Solution()
res = obj.findsumofseries(n)
print(res)