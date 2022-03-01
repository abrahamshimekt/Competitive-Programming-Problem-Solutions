# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None:
            return
        while curr.next:
            if curr.val == curr.next.val:
                nxt = curr.next.next
                curr.next = None
                curr.next = nxt
            else:
                curr = curr.next
        return head