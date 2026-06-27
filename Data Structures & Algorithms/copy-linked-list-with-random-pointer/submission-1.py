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
            return head
        orig = head
        dummy = Node(head.val, None, None)
        out = dummy

        d = {}

        d[head] = out

        while head.next:
            
            head = head.next

            cn = Node(head.val, None, None)

            out.next = cn

            out = out.next

            d[head] = out

        out2 = dummy
        while orig:
            if orig.random:
                out2.random = d[orig.random]

            out2 = out2.next
            orig = orig.next
        return dummy