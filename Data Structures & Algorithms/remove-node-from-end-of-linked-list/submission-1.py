# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i = 1

        # dummy = LinkedList(val=None,next=head)

        slow = head
        fast = head
        
        while fast and i<=n:

            fast = fast.next
            i+=1

        if fast == None:
            return head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next
        else:
            return slow.next

        return head

        



        

