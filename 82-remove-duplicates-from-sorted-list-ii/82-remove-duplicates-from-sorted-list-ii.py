# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        curr = head
        while curr:
            if curr.val not in dic:
                dic[curr.val] =1
            else:
                 dic[curr.val] +=1
            curr = curr.next
        dummy = curr = ListNode()
        for key in dic:
            if dic[key] ==1:
                curr.next = ListNode(key)
                curr = curr.next
        return dummy.next
                
        
        