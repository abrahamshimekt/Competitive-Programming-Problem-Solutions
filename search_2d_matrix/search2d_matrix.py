class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n*m-1
        # to solve this problem apply a binary search assuming the martix as a 1D
        # and find the mid value of a 1D array then convert it to rows and columns 
        # and check the mid value is the target or not
        
        while left <= right:

            mid = (left + right)//2

            # find the the row and column of the midian 
            row,col = mid//m,mid%m

            if matrix[row][col] == target:

                return True

            elif matrix[row][col] > target:
                right = mid-1

            else:
                left = mid+1

        return False
