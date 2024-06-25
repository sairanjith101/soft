
# n = 5
# names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]

# n = 4
# names = ["Apple", "Mango", "Orange", "Banana"]

n = 3
names = ["abc", "cb", "a"]

from typing import List

class Solution:
    def longest(self, n : int, names : List[str]) -> str:
        max_value = names[0]
        if len(names) == n:
            for name in names:
                if len(name) > len(max_value):
                    max_value = name
        return max_value
    
obj = Solution()
print(obj.longest(n, names))



# numbers = [1, 5, 3, 4, 0]
# max_value = numbers[0]
# for num in numbers:
#     if num > max_value:
#         max_value = num
# print(max_value)


