# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ITERATIVELY
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        curr = head

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

# time complexity: O(n)
# space complexity: O(1)

# RECURSIVELY
class Solution(object):
    def reverseListRecursive(self, head):
        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                next = curr.next
                curr.next = prev
                return reverse(next, curr)

        return reverse(head, None)

# time complexity: O(n)
# space complexity: O(n)