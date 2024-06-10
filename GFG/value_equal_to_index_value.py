# Option 1

# class Solution:
#     def valueEqualToIndex(self,Arr):
#         output = []
#         for i in range(1, len(Arr)+1):
#             for j in Arr:                
#                 if i == j:
#                     output.append(j)
#         return output

# Arr = [15, 2, 45, 12, 7]
# # Arr = [1]


# obj = Solution()
# res = obj.valueEqualToIndex(Arr)
# print(res)

# Option 2

class Solution:
    def valueEqualToIndex(self, arr, n):
        result = []
        for i in range(n):
            if arr[i] == i + 1:
                result.append(i + 1)
        return result

# Example usage:
arr1 = [15, 2, 45, 12, 7]
n1 = 5
obj = Solution()
res = obj.valueEqualToIndex(arr1, n1)
print(res)  # Output: 2

arr2 = [1]
n2 = 1
obj = Solution()
res = obj.valueEqualToIndex(arr2, n2)
print(res)  # Output: [1]

