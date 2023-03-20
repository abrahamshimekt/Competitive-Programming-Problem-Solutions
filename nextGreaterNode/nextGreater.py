# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        N = 0
        curr = head
        while curr:
            N +=1
            curr= curr.next
        answer = [0]*N
        stack = []
        curr = head
        index = 0
        while curr:
            while stack and stack[-1][0] < curr.val:
                nodeVal,currIndex = stack.pop()
                answer[currIndex] = curr.val
            stack.append([curr.val,index])
            curr = curr.next
            index +=1
        return answer        