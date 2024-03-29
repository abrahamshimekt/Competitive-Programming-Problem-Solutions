# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # the thing just starting from where the node is to be deleted shifting all nodes to the left
        prev = node
        curr = node.next
        while curr:
            prev.val = curr.val
            if not curr.next:
                break
            else:
                prev = curr
                curr = curr.next
        prev.next = None
        



        