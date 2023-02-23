# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_longest = 0
        left = 0
        chars = set()

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            max_longest = max(max_longest, right -left +1)
        return max_longest

# time complexity: O(n)
# space complexity: O(n)

# alternate solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = []
        max_length = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in hash:
                hash.append(s[r])
                if len(hash) > max_length:
                    max_length = len(hash)
                r += 1
            else:
                hash.remove(s[l])
                l += 1
        return max_length

