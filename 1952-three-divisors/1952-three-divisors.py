class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        i = 1
        while i <= n:
            if n%i == 0:
                divisors +=1
            i +=1
        if divisors != 3:
            return False
        return True
        
            