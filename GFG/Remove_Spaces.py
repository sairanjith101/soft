s = "geeks  for geeks"
# s = "    g f g"

class Solution:
    def modify(self, s):
        z = s.split(" ")
        return ("".join(z))
    
obj = Solution()
print(obj.modify(s))