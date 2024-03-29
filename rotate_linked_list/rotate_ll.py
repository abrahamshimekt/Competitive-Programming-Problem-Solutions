# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self,linked_list):
        prev = None
        curr = linked_list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next
        k = k%length
        if k == 0:
            return head
        start = length-k-1
        curr = head
        for index in range(start):
            curr = curr.next
        rotated = curr.next
        curr.next = None

        
        prev = head
        curr =  self.reverse_list(rotated)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
        
        
        
        