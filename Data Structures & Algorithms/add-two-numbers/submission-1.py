# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(None,None)
        out = dummy

        if not l1:
            return l2
        
        if not l2:
            return l1

        
        extra = 0

        while l1 and l2:

            curr_val = l1.val+l2.val+extra

            rem = curr_val%10

            carry = curr_val//10

            curr_node = ListNode(rem,None)
            out.next = curr_node
            out = out.next
            extra = carry

            l1 = l1.next
            l2 = l2.next

        j = None
        if not l1 and not l2:
                pass
        elif not l1:
            j = l2
        else:
            j = l1


        while j:
            curr_val = j.val +extra

            rem = curr_val%10

            carry = curr_val//10

            curr_node = ListNode(rem,None)
            out.next = curr_node
            out = out.next
            extra = carry

            j = j.next

        if extra:
            curr_node = ListNode(extra,None)
            out.next = curr_node
            out = out.next

        return dummy.next
        









