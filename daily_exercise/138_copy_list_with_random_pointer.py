"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        ht = {}
        p = head
        while p:
            new_node = Node(p.val, None, None)
            ht[p] = new_node
            p = p.next
        
        p = head
        while p:
            if p.next:
                ht[p].next = ht[p.next]
            if p.random:
                ht[p].random = ht[p.random]
            p = p.next
        
        return ht[head]
