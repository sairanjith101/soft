class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Implementation of the twoSum method
        # This method finds two numbers in the list 'nums' that add up to the 'target'
        # It returns their indices as a list [index1, index2]

        # Create a dictionary to store the complement of each number and its index
        num_dict = {}

        # Iterate through the list 'nums'
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num

            # If the complement is in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]

            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no such pair is found, return an empty list
        return []

# Example usage:
# Create an instance of the Solution class
sol = Solution()

# Define the input list of numbers and the target sum
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum method to find the indices of the two numbers that add up to the target
result = sol.twoSum(nums, target)
print(result) 

# Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
