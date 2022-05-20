# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        head_list = []
        while curr:
            head_list.append(curr.val)
            curr = curr.next
        head_list.pop(len(head_list)-n)
        curr = dummy = ListNode()
        for item in head_list:
            curr.next = ListNode(item)
            curr = curr.next
        return dummy.next
        
        