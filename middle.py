# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        curr = head
        length  = 0
        while curr:
            length +=1
            curr = curr.next
        curr  = head
        for i in range(length//2):
            curr = curr.next
        return curr

        
        # slow = head 
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow