# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        mag = list(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] in mag:
                mag.remove(ransomNote[i])
            else:
                return False 
        return True

# time complexity: O(n * m)
    # since we need to iterate over ransomNote in line 28, that's a nested loop
    # if we use a hashmap to store the letters in magazine, we could bring the time complexity down to O(n + m) since retrievals for dictionaries are O(1)
# space complexity: O(n)