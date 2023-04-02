# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=first=ListNode(next=head)
        first  = dummy.next
        first_prev = None
        index = 1
        last_part = None
        reversed_part = None
        while first:
            if index == left:
                prev = None
                if first_prev:
                    first_prev.next = None
                curr = first
                while index <=right:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    index +=1
                reversed_part = prev
                last_part=curr
                break
            else:
                first_prev = first
                first = first.next
                index +=1
       
        if left == 1:
            dummy.next= None
        if not dummy.next:
            dummy.next = reversed_part
        else: 
            first_curr = dummy.next
            while first_curr and first_curr.next:
                first_curr = first_curr.next
            first_curr.next = reversed_part
        
        last_curr = dummy.next
        while last_curr.next:

            last_curr = last_curr.next
        last_curr.next = last_part

        return dummy.next
        
        
        
      

                
                    
