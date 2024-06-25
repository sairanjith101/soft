n = 8
k = 3
arr = [1, 2, 3, 4, 5, 6, 7, 8]


from typing import List

class Solution:
    def swapKth(self, n: int, k: int, arr: List[int]) -> List[int]:
        if k <= 0 or k > n:
            return arr
        
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        
        return arr
    
    
obj = Solution()
print(obj.swapKth(n,k,arr))
        