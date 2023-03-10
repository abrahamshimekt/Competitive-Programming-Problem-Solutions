# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast , slow , prev = head , head , None
        while fast and fast.next:
            prev, slow,fast = slow,slow.next,fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left,right)
    def merge(self, left,right):
        node = merged = ListNode(None)
        while left and right:
            if left.val <= right.val:
                merged.next = left
                left = left.next
            else:
                merged.next = right
                right  = right.next
            merged = merged.next
        merged.next = left or right
        return node.next
                
        