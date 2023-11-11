# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1 
        before = None
        for _ in range(a):
           before = curr
           curr = curr.next
        last = list1
        for _ in range(b+1):
            last = last.next
        
        list2End = None
        curr = list2
        while curr.next:
            curr = curr.next
        list2End = curr
        if before:
            before.next = list2
            list2End.next = last
        else:
            list1 = list2
            list2End.next = last
        return list1
        
        


            