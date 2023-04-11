class Solution:
    def dfs(self,row,col):
        if row >=self.N or row <0 or col >=self.M or col <0 or self.image[row][col] != self.sourceColor or (row,col) in self.visited:
            return
        self.image[row][col] = self.color
        self.visited.add((row,col))
        for direction in self.directions:
            r,c = direction 
            self.dfs(row+r,col+c)
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.N = len(image)
        self.M = len(image[0])
        self.color = color
        self.visited = set()
        self.sourceColor = image[sr][sc]
        self.image = image
        self.directions = [(0,-1),(0,1),(-1,0),(1,0)]
        self.dfs(sr,sc)
        return self.image
       



        