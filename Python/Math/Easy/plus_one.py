# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert every item in list into a str, then joining the list into a string
        joined = ''.join(list(map(lambda x: str(x), digits)))

        # turning the string into an int, then adding 1
        add_one = int(joined)+1

        # converting strings back into int, then appending each digit into a list
        return [int(i) for i in str(add_one)]
    
# top solution
    def plusOne(digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]