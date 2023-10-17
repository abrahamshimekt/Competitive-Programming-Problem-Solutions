# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev  

        reversedL1 = helper(l1)
        reversedL2 = helper(l2)
        curr1 = reversedL1
        curr2 = reversedL2
        carry = 0
        dummy = ListNode()  
        curr = dummy
        while curr1 or curr2 or carry:
            total = carry
            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

        return helper(dummy.next) 
