# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        # find the half of the linked list first
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None

        # reverse the half of the linked lsut

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check whether the first half and the second of the linked list are similar
        curr = head
        second_half = prev
        while second_half:
            if second_half.val != curr.val:
                return False
            else:
                second_half = second_half.next
                curr = curr.next

        return True


        


        

        

        