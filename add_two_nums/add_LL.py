# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head =curr= ListNode()
        pointer1 = l1
        pointer2 = l2
        have = 0
        while pointer1 or pointer2:
            
            if pointer1 and pointer2:
                curr.next = ListNode((have +pointer1.val+pointer2.val)%10)
                have = (have + pointer1.val+pointer2.val)//10
                curr = curr.next
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            elif not pointer1 and pointer2:
                curr.next = ListNode((pointer2.val + have)%10)
                have = (pointer2.val + have)//10
                curr = curr.next
                pointer2 = pointer2.next
            elif not pointer2 and pointer1:
                curr.next = ListNode((pointer1.val + have)%10)
                have = (pointer1.val + have)//10
                curr = curr.next
                pointer1 = pointer1.next
            else:
                break
        if have:
            curr.next = ListNode(have)
            curr = curr.next
        return sum_head.next


            
            


        
        

