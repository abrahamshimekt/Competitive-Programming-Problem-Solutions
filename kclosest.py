import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        for i in range(n):
            for j in range(n-1):
                if math.sqrt(points[i][0]**2 + points[i][1]**2) < math.sqrt(points[j][0]**2 + points[j][1]**2):
                     points[j] ,points[i] = points[i], points[j]
        return points[:k]