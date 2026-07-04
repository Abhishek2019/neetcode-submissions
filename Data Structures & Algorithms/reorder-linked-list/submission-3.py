# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return None

        if not head.next:
            return None
        
        mid = head
        second = head

        while second and second.next:

            second = second.next.next
            mid = mid.next
        
        
        prev = None
        first = mid

        while first:

            temp = first.next
            first.next = prev
            prev = first
            first = temp
        
        print(prev.val, prev.next.val)

        first = head
        second = prev

        while second.next:

            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1
            
            first = t1
            second = t2

        





