class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num -3)/3
        if num == 0:
            return [-1,0,1]
        elif x < 0 or f"{x}"[-1] != "0":
            return []
        output = []
        for i in range(3):
            output.append(int(x) + i)
        return output
        