# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        merge = odds = ListNode()
        even_list = evens = ListNode()
        index = 1
        curr = head
        while curr:
            if index % 2 != 0:
                odds.next = ListNode(curr.val)
                odds = odds.next
                curr = curr.next
               
            else:
                evens.next = ListNode(curr.val)
                evens = evens.next
                curr = curr.next
            index +=1
        curr = even_list.next
        while curr:
            odds.next = curr
            odds = odds.next
            curr = curr.next
        return merge.next
        
        


       

