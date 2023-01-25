# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # find out how many pairs of letters there are in the input using two pointers
        # we'll add each letter t the hashset, and remove it once we find a pair
        # longest palindrome = pairs* 2 + 1 and if letters > 1

        letters = set()
        pairs = 0
 
        for letter in s:
            if letter in letters:
                pairs += 1
                letters.remove(letter)
            else:
                letters.add(letter)

        if len(letters) >= 1:
            return pairs*2 + 1
        else: 
            return pairs*2

# time complexity: O(n+m)
# space complexity: O(n)
