# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length +=1
        nth = length - n 
        prev = None
        curr = head
        while curr:
            if nth > 0:
                prev = curr
                curr = curr.next
                nth -=1
            else:
                if prev == None:
                    head = head.next
                    break
                else:
                    temp = curr.next
                    prev.next = curr.next
                    curr.next = None
                    curr = temp
                    break
        return head


            