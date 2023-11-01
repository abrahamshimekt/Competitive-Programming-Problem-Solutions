# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        head = stack[0]
        curr = head
        n = len(stack)
        for i in range(n-1):
            curr.next = stack[i+1]
            curr = curr.next
        return head
        