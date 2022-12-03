class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x
        for i in range(x):
            if i * i == x:
                return i
            elif i*i > x:
                return i-1
        return i
            
        