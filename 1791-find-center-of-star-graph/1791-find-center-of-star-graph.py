class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0][0]
        y = edges[0][1]
        if edges[1][0]==x or edges[1][1] ==x:
            return x
        return y