class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move = 0
        for i in range(len(seats)):
            move += abs(seats[i]-students[i])
        return move