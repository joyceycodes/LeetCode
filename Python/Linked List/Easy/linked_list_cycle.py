# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # stores all of the nodes that we've seen already
        hash = set()

        while head:
            # if we're coming across a node that we've already seen, that means there's a cycle
            if head in hash:
                return True
            if head.next == None:
                return False
            hash.add(head)
            head = head.next

# time complexity: O(n)
# space complexity: O(n)

# can also be solved using a fast and slow pointer (Floyd's tortoise and hare)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# time complexity: O(n)
# space complexity: O(1)