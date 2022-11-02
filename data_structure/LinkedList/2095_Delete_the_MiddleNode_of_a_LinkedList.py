from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution: two pointers
        """
        if not head.next or not head:
            return None

        dummy = ListNode(-1, head)
        slow, fast = dummy, head

        cnt = 0
        while fast:
            cnt += 1
            fast = fast.next
            if cnt % 2 == 0:
                slow = slow.next

        slow.next = slow.next.next

        return head
