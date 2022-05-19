# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_length = 0
        curr = head
        while curr != None:
            head_length +=1
            curr = curr.next
        mid = head_length//2
        while head != None and mid >0:
            mid -=1
            head = head.next
        return head
        