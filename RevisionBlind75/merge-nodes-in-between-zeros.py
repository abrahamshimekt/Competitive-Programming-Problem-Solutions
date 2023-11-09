# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        right = head.next
        currSum = 0
        while right:
            if right.val == 0:
                if currSum > 0:
                    curr.next = ListNode(currSum)
                    curr = curr.next

                currSum = 0
                
            else:
                currSum += right.val
            right = right.next
        return dummy.next
        

                
            
        