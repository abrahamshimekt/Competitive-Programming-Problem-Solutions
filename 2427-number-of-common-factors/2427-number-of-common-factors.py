class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        num = 0
        if a >= b :
            num = a
        else:
            num = b
        factors = 0
        for i in range(1,num+1):
            if a % i == 0 and b % i ==0:
                factors +=1
        return factors
            
            