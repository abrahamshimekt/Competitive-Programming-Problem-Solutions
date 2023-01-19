def row_col_count(grid,n,m):
    
    row_count = {}
    col_count = {}

    for row in range(n):
        for col in range(m):
            if (row,grid[row][col]) not in row_count:
                row_count[(row,grid[row][col])] = 1
            else:
                 row_count[(row,grid[row][col])] += 1
            if (col,grid[row][col])  not in col_count:
                col_count[(col,grid[row][col])] = 1
            else:
                col_count[(col,grid[row][col])] += 1
    return row_count,col_count
                
    
    
        
n,m = map(int,input().split())

grid = []

for index in range(int(n)):
    grid.append(input())
    
row_count,col_count = row_col_count(grid,n,m)

word = []

for row in range(int(n)):
    for col in range(int(m)):
        
       if row_count[(row,grid[row][col])] <2 and col_count[(col,grid[row][col])] <2:
            word.append(grid[row][col])

print(''.join(word))
        

