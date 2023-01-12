 def minDeletionSize(self, strs: List[str]) -> int:
       

        rows= len(strs)
        cols = len(strs[0])
        delted_cols = 0

        for col in range(cols):

            not_sorted = False
            
            for row in range(rows-1):
                if strs[row][col] > strs[row+1][col]:
                    not_sorted = True
                    break
                    
            if not_sorted:
                delted_cols +=1

        return delted_cols

                
