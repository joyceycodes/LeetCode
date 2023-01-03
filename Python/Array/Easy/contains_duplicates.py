# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# my solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=0
            else:
                return True
        
        return False

# time complexity : O(n)
# space complexity: O(n)

# top solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (len(nums) != len(set(nums)))