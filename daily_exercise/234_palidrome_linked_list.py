# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums_list = []
        while head:
            nums_list.append(head.val)
            head = head.next
        begin, end = 0, len(nums_list) -1
        while begin <= end:
            if nums_list[begin] != nums_list[end]:
                return False 
            begin += 1
            end -= 1
        
        return True
