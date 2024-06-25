class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
a = 50
b = 500

obj = Solution()
print(obj.gcd(a,b))

# class Solution:
#     def gcd(self, a : int, b : int) -> int:
#         i = 1
#         l = []
#         for i in range(1,min(a, b) + 1):
#             if a % i == 0 and b % i == 0:
#                 l.append(i)
#             else:
#                 i+=1
#         return max(l)
# a = 119
# b = 68


# obj = Solution()
# print(obj.gcd(a,b))