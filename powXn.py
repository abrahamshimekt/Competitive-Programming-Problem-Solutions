class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = n
        orginalX = x
        if  n < 0:
            result = 1
            n = -n
            while n > 0:
                if n & 1:
                    result /= x
                x *=x
                n >>=1
           
            return result
                 
        else:
            result = 1
            while n > 0:
                if n & 1:
                    result *= x
                x *=x
                n >>=1
          
            return result

        
