# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid_next = slow.next
        slow.next = None

        first=None
        second = mid_next

        while second:
            nxt = second.next
            second.next = first

            first = second
            second = nxt

        i = 0

        while first:

            nxt = head.next
            fnxt = first.next

            head.next = first
            head.next.next = nxt
            head = head.next.next
            first = fnxt
            

        