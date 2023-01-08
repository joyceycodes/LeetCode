# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = ''

        for letter in s.lower():
            # isalnum() checks if it's a number OR letter
            if letter.isalnum() :
                chars += letter

        # check if the string is the same as the reversed string
        return chars == chars[::-1]


# time complexity: O(n)
# space complexity: O(n)


# another solution with better memory and does not rely on a built-in function, isalnum()
class Solution(object):
    # creating a helper function that returns true if it's a letter or number by looking up the ASCII number
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            # we want to do l < r to make sure it doesn't go out of bounds and only consider chars that are alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l = l + 1
            r = r - 1

        return True

# time complexity: O(n)
# space complexity: O(1)