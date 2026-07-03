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

        if head:
            n_head = Node(head.val, None, None)
        else:
            return None

        map = {}

        map[head] = n_head

        first = head
        

        while first:

            if first not in map:

                map[first] = Node(first.val, None, None)

            first = first.next
        
        print(map)
        first  = head
        while first:

            if first.next:
                map[first].next = map[first.next]
            else:
                map[first].next = None

            if first.random:
                map[first].random = map[first.random]
            else:
                map[first].random = None

            first = first.next




        return n_head





        