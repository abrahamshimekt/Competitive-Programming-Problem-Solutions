# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            prev = head
            curr = head.next
            while curr:
                if prev.val == curr.val:
                    temp = curr.next
                    prev.next = curr.next
                    curr.next = None
                    curr = temp
                else:
                    prev = curr
                    curr = curr.next
            return head


