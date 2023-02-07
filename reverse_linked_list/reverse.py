# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headList = []
        curr = head
        while curr:
            headList.append(curr.val)
            curr = curr.next
        headList = headList[::-1]
        if headList:
            head = ListNode(headList[0])
            curr = head
            for i in range(1,len(headList)):
                if i !=0:
                    node = ListNode(headList[i])
                    curr.next = node
                    curr = curr.next
            return head
        return None

        