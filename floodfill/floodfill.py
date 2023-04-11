class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])

        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        stack = [(sr,sc)]

        visited = set()
        sourceColor = image[sr][sc]

        while stack:
            row,col = stack.pop()
            for direction in directions:
                r,c = direction
                if 0<= row+r <N and 0<= col+c<M:
                    if image[row+r][col+c] == sourceColor and (row+r,col+c) not in visited:
                        stack.append((row+r,col+c))
            image[row][col] = color
            visited.add((row,col))
        return image



        