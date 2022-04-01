# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = []
        
        node = head.next
        while node:
            queue.append(node.val)
            node = node.next
        node = head   
        while queue:
            node = node.next
            end = queue.pop()
            node.val = end
        
            if queue:
                node = node.next
                begin = queue.pop(0)
                node.val = begin

        return head
