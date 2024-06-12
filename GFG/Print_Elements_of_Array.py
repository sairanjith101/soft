# n = 5
# arr = [1, 2, 3, 4, 5]

class Solution:
	def printArray(self,arr, n):
		for i in arr:
			if len(arr) == n:
				print(i, end=" ")

n = 4
arr = [2, 3, 5, 5]

obj = Solution()
obj.printArray(arr,n)