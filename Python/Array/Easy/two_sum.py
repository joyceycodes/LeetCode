# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        for i in range(len(nums)):
            print(nums[i])
            for j in range(i+1,len(nums)):
                print(nums[j])
                if (nums[i] + nums[j]) == target:
                    return i, j

# time complexity: O(n^2)
# space complexity: O(1)

# solution with better time complexity using a hashmap to store value and indexes
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indexes of the two nums in nums that add up to the target
        Hashmap = {}
        for index, value in enumerate(nums):
            key = target - value
            if key in Hashmap:
                return [Hashmap[key], index]
            else:
                Hashmap[value] = index

# time complexity: O(n)
# space complexity: O(n)