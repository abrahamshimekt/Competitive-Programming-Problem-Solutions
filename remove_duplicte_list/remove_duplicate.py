# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        curr = head
        while curr:
            if curr.val not in nodes:
                nodes[curr.val] = 1
            else:
                nodes[curr.val] +=1
            curr = curr.next
        curr = ListNode()
        dummy = ListNode(next=curr)
        for node in nodes:
            if nodes[node] ==1 :
                curr.next = ListNode(node)
                curr = curr.next
        return dummy.next.next


        