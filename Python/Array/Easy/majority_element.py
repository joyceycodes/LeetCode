# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+= 1
        
        max = 0
        num = 0

        for k,v in count.items():
            if v > max:
                max = v
                num = k
        return num


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashset = set(nums)
        count = 0
        num = 0
        for i in hashset:
            if nums.count(i) > count:
                count = nums.count(i)
                num = i
        return num