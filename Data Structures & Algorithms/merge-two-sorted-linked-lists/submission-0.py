# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        out = None

        new = ListNode(val = None)

        out = new

        while list1 and list2:
            
            if list1.val <= list2.val:

                new.next = list1
                new = new.next
                list1 = list1.next


            elif list1.val > list2.val:
                new.next = list2
                new = new.next
                list2 = list2.next

        if list1 and not list2:
            new.next = list1

        else:
            if list2 and not list1:
                new.next = list2

        return out.next



