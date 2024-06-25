# N = 7
# X = 0
# Arr = [1, 2, 8, 10, 11, 12, 19]

N = 3
X = 3
Arr = [3, 3, 3]


class Solution:
    def getMoreAndLess(self,arr, n, x):
        count_less = 0
        count_more = 0
        for i in arr:
            if i <= x:
                count_less += 1
            if i >= x:
                count_more += 1

        return count_less, count_more

# N = 7
# X = 5
# Arr = [1, 2, 8, 10, 11, 12, 19]

obj = Solution()
print(obj.getMoreAndLess(Arr, N, X))