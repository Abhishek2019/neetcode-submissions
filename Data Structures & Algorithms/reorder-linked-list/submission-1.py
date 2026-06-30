# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        #get mid

        mid = head
        last = head

        while last and last.next:

            mid = mid.next
            last = last.next.next


        def make_reverse(node):
            prev = None
            while node:
                second = node.next
                node.next = prev
                prev = node
                node = second

            return prev


        second = make_reverse(mid)

        first = head

        while second.next:

            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2





