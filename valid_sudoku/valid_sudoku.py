class Solution:
    def valid_row(self,board):

        for row in range(9):
            lookup = set()
            for col in range(9):
                if board[row][col].isdigit() :
                    if  board[row][col] in lookup:
                        return False
                    else:
                        lookup.add(board[row][col])
        return True

    def valid_col(self,board):
        for col in range(9):
            lookup = set()
            for row in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in lookup:
                        return False
                    else:
                        lookup.add(board[row][col])
        return True

    def valid_3by3(self,board,top,left):
        lookup = set()
        for row in range(top,top+3):
            for col in range(left,left+3):
                if board[row][col].isdigit():
                    if board[row][col] in lookup:
                        return False
                    else:
                        lookup.add(board[row][col])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not self.valid_row(board):
            return False
        elif not self.valid_col(board):
            return False
        else:
            for row in range(0,9,3):
                for col in range(0,9,3):
                    if not self.valid_3by3(board,row,col):
                        return False
            return True