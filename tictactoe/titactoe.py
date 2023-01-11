class Solution:
    def row_winner(self,board):
        X_winner = False
        O_winner = False
        for row in range(3):
            if board[row][0] == "X":
                for col in range(2):
                    if board[row][col] != board[row][col+1]:
                        break
                else:
                    X_winner = True
                    break
            elif board[row][0] == "O":
                for col in range(2):
                    if board[row][col] != board[row][col+1]:
                        break
                else:
                    O_winner = True
                    break
            else:
                continue

        return X_winner,O_winner

    def col_winner(self,board):
        X_winner = False
        O_winner = False
        for col in range(3):
            if board[0][col] == "X":
                for row in range(2):
                    if board[row][col] != board[row+1][col]:
                        break
                else:
                    X_winner = True
                    break
            elif board[0][col] == "O":
                for row in range(2):
                    if board[row][col] != board[row+1][col]:
                        break
                else:
                    O_winner = True
                    break
            else:
                continue

        return X_winner,O_winner
    def diagonal_main(self,board):
        X_winner = False
        O_winner = False
        if board[0][0] == "X":
            if board[0][0] == board[1][1] == board[2][2]:
                X_winner = True
        elif board[0][0] == "O":
            if board[0][0] == board[1][1] == board[2][2]:
                O_winner = True
        
        return X_winner,O_winner
    def diagonal(self,board):
        X_winner = False
        O_winner = False
        if board[0][2] == "X":
            if board[0][2] == board[1][1] == board[2][0]:
                X_winner = True
        elif board[0][2] == "O":
            if board[0][2] == board[1][1] == board[2][0]:
                O_winner = True
        return X_winner,O_winner
        

    def validTicTacToe(self, board: List[str]) -> bool:

        X_O = {"X":0,"O":0}

        for row in range(3):
            for col in range(3):
                if board[row][col] == "X":
                    X_O["X"] +=1
                elif board[row][col] == "O":
                    X_O["O"] +=1
                else:
                    continue

        X_row_winner = self.row_winner(board)[0]
        X_col_winner = self.col_winner(board)[0]
        X_diagonal_main = self.diagonal_main(board)[0]
        X_diagonal = self.diagonal(board)[0]

        O_row_winner = self.row_winner(board)[1]
        O_col_winner = self.col_winner(board)[1]
        O_diagonal_main = self.diagonal_main(board)[1]
        O_diagonal = self.diagonal(board)[1]

        is_X_winner = (X_row_winner or X_col_winner or X_diagonal or X_diagonal_main )
        is_O_winner = (O_row_winner or O_col_winner or O_diagonal or O_diagonal_main )

        if X_O["O"] >X_O["X"]:
            return False
        elif X_O["X"] - X_O["O"] > 1:
            return False
        elif X_O["X"] - X_O["O"] == 1 and is_X_winner :
            return True
        elif X_O["X"] - X_O["O"] == 0 and is_O_winner:
            return True
        elif X_O["X"] - X_O["O"] == 1  and not (is_X_winner or is_O_winner ):
            return True
        elif X_O["X"] - X_O["O"] == 0 and not (is_X_winner or is_O_winner ):
            return True
        else:
            return False
        