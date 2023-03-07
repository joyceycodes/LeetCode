# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head

        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        
        return p2

# brrute force solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        middle = len(nodes)//2
        return nodes[middle]