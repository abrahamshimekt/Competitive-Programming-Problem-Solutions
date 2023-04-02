# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
           nums.append(curr.val)
           curr = curr.next
        for outer in range(1,len(nums)):
            num = nums[outer]
            inner = outer -1
            while inner > -1:
                if nums[inner] >= num:
                    nums[inner+1] = nums[inner]
                    inner -=1
                else:
                    nums[inner+1] = num
                    break
            if inner == -1:
                nums[0] = num
        dummy = curr = ListNode()
        for index in range(len(nums)):
            curr.next = ListNode(nums[index])
            curr = curr.next
        return dummy.next
            
                



                    

