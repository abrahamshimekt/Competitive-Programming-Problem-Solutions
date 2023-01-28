def main_diagonal_sum(grid,m,n):
    main_diagonal = {}
   
    for col in range(n):
        c = col
        r = 0
        curr_sum = 0
        row_col = []
        while r < m and c < n:
            curr_sum += int(grid[r][c])
            row_col.append((r,c))
            r +=1
            c +=1
        for pair in row_col:
            main_diagonal[pair] = curr_sum
    
    for row in range(1,m):
        r = row
        c = 0
        curr_sum = 0
        row_col = []
        while r < m and c < n:
            curr_sum += int(grid[r][c])
            row_col.append((r,c))
            r +=1
            c +=1
        for pair in row_col:
            main_diagonal[pair] = curr_sum
            
    return main_diagonal
def sub_diagonal_sum(grid,m,n):
    sub_diagobal = {}
    
    for col in range(n):
        c = col
        r = 0
        curr_sum = 0
        row_col = []
        while r < m and c > -1:
            curr_sum += int(grid[r][c])
            row_col.append((r,c))
            r +=1
            c -=1
        for pair in row_col:
            sub_diagobal[pair] = curr_sum
    
    for row in range(1,m):
        r = row
        c = n-1
        curr_sum = 0
        row_col = []
        while r < m and c > -1:
            curr_sum += int(grid[r][c])
            row_col.append((r,c))
            r +=1
            c -=1
        for pair in row_col:
            sub_diagobal[pair] = curr_sum
    return sub_diagobal
    
 
 
    
T = int(input())
for t in range(T):
    m,n = map(int,input().split())
    grid = []
    for line in range(m):
        grid.append(input().split())
    main_diagonal =  main_diagonal_sum(grid,m,n)
    sub_diagonal = sub_diagonal_sum(grid,m,n)
    max_attack = 0
    for row in range(m):
        for col in range(n):
            max_attack = max(max_attack,main_diagonal[(row,col)] + sub_diagonal[(row,col)] - int(grid[row][col]))
    print(max_attack)