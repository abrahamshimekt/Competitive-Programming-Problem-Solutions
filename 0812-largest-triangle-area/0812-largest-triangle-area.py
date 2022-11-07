class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j + 1,n):
                    a =((points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2)**0.5
                    b = ((points[k][0]-points[i][0])**2 + (points[k][1]-points[i][1])**2)**0.5
                    c = ((points[k][0]-points[j][0])**2 + (points[k][1]-points[j][1])**2)**0.5
                    s = (a + b +c)/2
                    
                    area = (s*(s-a)*(s-b)*(s-c))
                    if area >=0:
                        max_area = max(max_area,area**0.5)
        return max_area
                    