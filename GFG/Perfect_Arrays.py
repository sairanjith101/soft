n = 5
arr = [1, 2, 3, 2, 1]

# n = 5
# arr = [1, 2, 3, 4, 5]

from typing import List


class Solution:
    def isPerfect(self, n : int, arr : List[int]) -> bool:
        
        x = arr[::-1]
        return x == arr

obj = Solution()
print(obj.isPerfect(n,arr))























# from typing import List


# class Solution:
#     def isPerfect(self, n : int, arr : List[int]) -> bool:
#         x = arr[::-1]
#         if (arr == x):
#             return "PERFECT"
#         else:
#             return "NOT PERFECT"
        
# obj = Solution()
# print(obj.isPerfect(n,arr))