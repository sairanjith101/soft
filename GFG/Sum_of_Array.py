class Solution:
	def _sum(self,arr, n):
		res = 0
		if len(arr) == n:
			for i in arr:
				res += i
		return res
   		

# arr = [1, 2, 3, 4]
# n = 4

arr = [1,3,3]
n = 3

obj = Solution()
print(obj._sum(arr,n))

