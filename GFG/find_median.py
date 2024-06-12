# arr = [90,100,78,89,67]
# arr = [10,20,30,40]

# arr_sorted = sorted(arr)

# x = len(arr_sorted) // 2

# if len(arr_sorted) % 2 != 0:
#     print(arr_sorted[x])
# elif len(arr_sorted) % 2 == 0:
#     res = ((arr_sorted[x] + (arr_sorted[x-1])) // 2)
#     print(res)

class Solution:
    def find_median(self, v):
        arr_sorted = sorted(v)
        x = len(arr_sorted) // 2

        if len(arr_sorted) == N:
            if len(arr_sorted) % 2 != 0:
                return arr_sorted[x]
            else:
                res = (arr_sorted[x] + (arr_sorted[x-1])) // 2
                return res

        
N = 5
arr = [90,100,78,89,67]
# arr = [10,20,30,40]
# arr = [56,67,30,79]
obj = Solution()
print(obj.find_median(arr))

