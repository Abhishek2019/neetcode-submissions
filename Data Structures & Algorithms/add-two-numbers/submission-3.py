# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        n1 = l1
        n2 = l2

        out = ListNode(0, None)

        dummy = out

        carry = 0
        while l1 or l2:

            n1 = None
            n2 = None

            if l1:
                n1 = l1.val

            else:
                n1 = 0

            if l2:
                n2 = l2.val
            else:
                n2 = 0

            
            curr = n1+n2+carry

            digit = curr//10
            remind = curr%10

            carry = digit

            out.next = ListNode(remind,None)

            out = out.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            out.next = ListNode(carry,None)
        return dummy.next








