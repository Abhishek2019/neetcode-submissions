# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy
        first = head

        final = dummy

        count = 0

        while count <n and final.next:

            final = final.next
        
            count+=1
        print(first.val, final.val)

        while final.next:
            final = final.next
            prev = first
            first = first.next

        prev.next = first.next

        return dummy.next





        