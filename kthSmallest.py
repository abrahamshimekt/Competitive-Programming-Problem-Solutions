from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        nums = []

        for row in range(n):
            for col in range(n):
                nums.append(matrix[row][col])

        heapify(nums)
        kthSmallest = 0

        for operation in range(k):
            kthSmallest = heappop(nums)
            
        return kthSmallest
             
        
