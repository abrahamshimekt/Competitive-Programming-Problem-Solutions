def right(grid,m,row,col):
    
     
    for c in range(col+1,m):
        if grid[row][c] == grid[row][col]:
            return False
    return True
def left(grid,row,col):
    
   
    for c in range(col-1,-1,-1):
        if  grid[row][c] == grid[row][col]:
            return False
    return True
def down(grid,n,row,col):
    
    for r in range(row+1,n):
        if grid[r][col] == grid[row][col]:
            return False
        
    return True
def up(grid,row,col):
   
   
    for r in range(row-1,-1,-1):
        if grid[r][col] == grid[row][col]:
            return False
 
    return True
    
        
n,m = input().split()
grid = []
for index in range(int(n)):
    grid.append(input())
word = []
for row in range(int(n)):
    for col in range(int(m)):
        if (right(grid,int(m),row,col) and left(grid,row,col)) and (up(grid,row,col) and down(grid,int(n),row,col)):
                word.append(grid[row][col])
print(''.join(word))