# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for col in range(n)] for row in range(m)]
      
        top = left = 0
        bottom ,right= m-1,n-1
        curr = head
        while left <= right or top <= bottom:
            for i in range(left,right+1) if top <= bottom else []:
                matrix[top][i] = curr.val if curr else -1
                curr = curr.next if curr else None
               
            top +=1
            for j in range(top, bottom+1) if left <= right else []:
                matrix[j][right] = curr.val if curr else -1
                curr = curr.next if curr else None
              
            right -=1
            for k in range(right,left-1,-1) if top <= bottom else []:
                
                matrix[bottom][k] = curr.val if curr else -1
                curr = curr.next if curr else None
               
            bottom -=1
            for l in range(bottom,top-1,-1) if left <= right else []:
               
                matrix[l][left] = curr.val if curr else -1
                curr = curr.next if curr else None
              
            left +=1
        return matrix


         
        