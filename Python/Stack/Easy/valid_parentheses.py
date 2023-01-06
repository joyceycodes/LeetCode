# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# TRUE: '{}[]()', '{[()]}'
# FALSE: '[(])'

# APPROACH
# Since every opening parentheses will need a corresponding closing parentheses in the correct order, it makes sense for us to use a STACK that tracks all the open parentheses. Each time we hit a close parentheses, we'll check if the last item in the stack is the corresponding open parentheses since they need to be closed in order. If it is, we'll remove the last item from the stack.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # creating a stack that will hold all the open parentheses
        stack = []

        # creating a hashmap to match the correct parentheses type
        hashmap = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }

        for c in s: 
            # if c is a closing parentheses
            if c in hashmap:
                # check if stack is not empty, is the last item in stack, and that it's the correct open paren
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            # if it's an open parentheses, we'll add it to the stack
            else:
                stack.append(c)

        # return True is the stack is empty
        return True if not stack else False

# time complexity: O(n)
# space complexity: O(n)