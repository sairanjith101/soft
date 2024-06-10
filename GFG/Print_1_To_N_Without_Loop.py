# def add(n):
#     if n > 0:
#         add(n - 1)
#         print(n)

# n = int(input("Enter a value for N: "))
# add(n)

class Solution:
    def printNos(self, N):
        if N > 0:
            self.printNos(N - 1)
            print(N, end=" ")

N = int(input("Enter a value: "))
obj = Solution()
obj.printNos(N)