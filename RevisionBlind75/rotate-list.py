# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        curr = head

        while curr:
            n+=1
            curr = curr.next
        k = k%n

        second = None
        curr = head 
        for _ in range(k):
            second = curr
            curr = curr.next
        first = head
        prev = None
        while second and second.next:
            prev = first
            first = first.next
            second = second.next
        if second:
            newHead = first
            prev.next = None
            second.next = head
        else:
            newHead = head
        return newHead
        
        
            

        
