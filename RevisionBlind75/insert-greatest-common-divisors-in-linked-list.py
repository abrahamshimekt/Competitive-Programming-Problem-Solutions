# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
       

        def findGCD(a,b):
            if b==0:
                return a
            return findGCD(b,a%b)
        if not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            gcd = findGCD(prev.val,curr.val)
            newNode = ListNode(gcd)
            prev.next = newNode
            newNode.next = curr
            prev = curr 
            curr = curr.next
        return head
        

        