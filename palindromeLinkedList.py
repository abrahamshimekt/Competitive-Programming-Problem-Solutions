# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        nums =[]
        if not head:
            return True
        while curr:
            nums.append(curr.val)
            curr = curr.next
        i = 0
        j = len(nums)-1
        while i <=j:
            if nums[i] != nums[j]:
                return False
            else:
                i +=1
                j -=1
        return True
        # prev = None
        # current = head
        # while current:
        #     nxt = current.next
        #     current.next,prev = prev,current
        #     current = nxt
        # return True if prev == head else False