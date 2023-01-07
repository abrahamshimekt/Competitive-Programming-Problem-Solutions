class Solution:
    def move_right(self,queens_set,king):

        row = king[0]
        col = king[1]

        for index in range(col + 1,8):
            if (row,index) in queens_set:
                return [row,index]
        return []
        
    def move_left(self,queens_set,king):

        row = king[0]
        col = king[1]

        for index in range(col-1,-1,-1):
            if (row,index) in queens_set:
                return [row,index]

        return []

    def move_up (self,queens_set,king):

        row = king[0]
        col = king[1]

        for index in range(row - 1,-1,-1):
            if (index,col) in queens_set:
                return [index,col]

        return []

    def move_down (self,queens_set,king):

        row = king[0]
        col = king[1]

        for index in range(row + 1,8):
            if (index,col) in queens_set:
                return [index,col]

        return []

    def move_left_up(self,queens_set,king):

        row = king[0]-1
        col = king[1] -1

        while row  > -1 and col > -1:
            if (row,col) in queens_set:
                return [row,col]
            else:
                row -= 1
                col -= 1

        return []

    def move_right_bottom(self,queens_set,king):

        row = king[0] + 1
        col = king[1]+1

        while row <8 and col < 8:
            if (row,col) in queens_set:
                return [row,col]
            else:
                row +=1
                col +=1

        return []

    def move_right_up(self,queens_set,king):

        row = king[0] -1
        col = king[1]+1

        while row > -1 and col < 8:
            if (row,col) in queens_set:
                return [row,col]
            else:
                row -=1
                col +=1

        return []

    def move_left_bottom(self,queens_set,king):

        row = king[0]+1
        col = king[1]-1
        while row < 8 and col > -1:
            if (row,col) in queens_set:
                return [row,col]
            else:
                row +=1
                col -=1
        return []




    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        queens_set = set()

        for queen in queens:
            queens_set.add(tuple(queen))
      
        attackers = []

        if self.move_right(queens_set,king):
            attackers.append(self.move_right(queens_set,king))

        if self.move_left(queens_set,king):
            attackers.append(self.move_left(queens_set,king))

        if self.move_up(queens_set,king):
            attackers.append(self.move_up(queens_set,king))

        if self.move_down(queens_set,king):
            attackers.append(self.move_down(queens_set,king))

        if self.move_left_up(queens_set,king):
            attackers.append(self.move_left_up(queens_set,king))

        if self.move_right_bottom(queens_set,king):
            attackers.append(self.move_right_bottom(queens_set,king))

        if self.move_right_up(queens_set,king):
            attackers.append(self.move_right_up(queens_set,king))

        if self.move_left_bottom(queens_set,king):
            attackers.append(self.move_left_bottom(queens_set,king))

        return attackers

       

        





