# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i in s:
            s_count = s.count(i)
            t_count = t.count(i)
            if s_count != t_count:
                return False
        return True

# time complexity: O(n) or O(s+t)
# space complexity: O(n)

# this solution has same time complexity but is less code and requires importing from the collections module
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


# this solution is better for memory
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
