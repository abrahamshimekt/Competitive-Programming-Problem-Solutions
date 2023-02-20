# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        fast = head
        while fast:
            if fast in nodes:
                return True
            else:
                nodes.add(fast)
                fast = fast.next
        return False