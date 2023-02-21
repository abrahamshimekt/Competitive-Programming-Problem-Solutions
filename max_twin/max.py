# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        curr = prev
        first = head
        max_twin_sum = 0
        while curr:
            max_twin_sum = max(max_twin_sum,curr.val + first.val)
            curr = curr.next
            first = first.next
        return max_twin_sum



