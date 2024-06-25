# Option 1

# n = 5
# key = 2
# arr = [10, 20, 30, 40, 50]

n = 7
key = 4
arr = [10, 20, 30, 40, 50, 60, 70]

from typing import List


class Solution:
    def findElementAtIndex(self, n : int, key : int, arr : List[int]) -> int:
        for i in range(len(arr)):
            if len(arr) == n:
                if i == key:
                    return arr[i]

obj = Solution()
print(obj.findElementAtIndex(n,key,arr))


# Option 2

# n = 5
# key = 2
# arr = [10, 20, 30, 40, 50]

n = 7
key = 4
arr = [10, 20, 30, 40, 50, 60, 70]

from typing import List

class Solution:
    def findElementAtIndex(self, n : int, key : int, arr : List[int]) -> int:
        if len(arr) == n:
            return arr[key]
                

obj = Solution()
print(obj.findElementAtIndex(n,key,arr))