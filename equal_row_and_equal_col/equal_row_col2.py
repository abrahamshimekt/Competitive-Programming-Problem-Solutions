def equalPairs(self, grid: List[List[int]]) -> int:

        size = len(grid)
        pairs_count = 0

        # brute force way in O(N^3) time complexity

        for row in range(size):

            curr_row = grid[row]

            for col in range(size):

                for index in range(size):
                    
                    # check the ith element of the row and the column are equal or not
                    if curr_row[index] != grid[index][col]:
                        break
                else:
                    pairs_count +=1

        return pairs_count