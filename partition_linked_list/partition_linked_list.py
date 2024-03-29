# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        partitioned_list = less_x = ListNode()
        curr = head
        prev = None
        while curr:
            if curr.val < x:
                less_x.next = ListNode(curr.val)
                less_x = less_x.next
                if not prev:
                    head = head.next
                    curr = head
                else:
                    temp = curr.next
                    prev.next = curr.next
                    curr.next = None
                    curr = temp
            else:
                prev = curr
                curr = curr.next
        
        curr = head
        while curr:
            less_x.next = curr
            less_x = less_x.next
            curr = curr.next
        return partitioned_list.next
        
            
        