class Solution:
    def minimumSum(self, num: int) -> int:
        num =sorted(list (f"{num}"))
        x = num[0] + num[3]
        y = num[1] + num[2]
        return int(x) + int(y)
        
        
        