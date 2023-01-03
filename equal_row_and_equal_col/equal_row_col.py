def equalPairs(self, grid: List[List[int]]) -> int:
       
        row_counts = {}
        col_counts = {}
        size = len(grid)

         # count the rows similar
        for row in range(size):

            curr_row =' '.join([str(num) for num in grid[row]])
            if curr_row not in row_counts:
                row_counts[curr_row] = 1
            else:
                 row_counts[curr_row] += 1

         # count cols similar
        for col_ in range(size):
            curr_col = []
            for row_ in range(size):
                curr_col.append(str(grid[row_][col_]))
            curr_col = ' '.join(curr_col)
            if curr_col not in col_counts:
                col_counts[curr_col] =1
            else:
                col_counts[curr_col] +=1
        
        pairs = 0

        # if a row found in columns count, then make a multiplication rule which says 
        # if there are m buses to go from A to B and n buses from B to C, then there are 
        # m*n buses to go from A to C

        for row_count in row_counts:
            if row_count in col_counts:
                pairs += row_counts[row_count]*col_counts[row_count]
                
        return pairs